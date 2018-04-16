#include <stdio.h>
#include <sqlite3.h>
/* #include <sqlite3ext.h> */

#define track() printf("track: %s:%d\n", __func__, __LINE__)

static int _sql_callback(void *notused, int argc, char **argv, char **szColName)
{
    int i = 0;

    printf("notused:%p, argc:%d\n", notused, argc);
    for (i = 0; i < argc; i++)
    {
        printf("%s = %s\n", szColName[i], argv[i] == 0 ? "NULL" : argv[i]);
    }
    printf("\n");

    return 0;
}

static void firstchar(sqlite3_context *context, int argc, sqlite3_value **argv)
{
    if (argc == 1) {
        const char *text = sqlite3_value_text(argv[0]);
        if (text && text[0]) {
            char result[2];
            result[0] = text[0]; result[1] = '\0';
            sqlite3_result_text(context, result, -1, SQLITE_TRANSIENT);
            return;
        }
    }
    sqlite3_result_null(context);
}

static void onTrigger(sqlite3_context *context, int argc, sqlite3_value **argv)
{
    printf("onTrigger argc = %d\n", argc);
}

int main(int argc, char** argv)
{
    const char *sSQL1 = "create table users(userid varchar(20) PRIMARY KEY, age int, birthday datetime);";
    const char *sSQL1_2 = "create table users2(userid varchar(20) PRIMARY KEY, age int, birthday datetime);";
    const char *sSQL2 = "insert into users values('wang', 20, '1989-5-4');";
    const char *sSQL2_2 = "insert into users2 values('wang', 30, '1989-5-5');";
    const char *sSQL3 = "select * from users;";
    const char *sSQL4 = "select firstchar(\"aa\");";

    const char *sSQL5 = "\
        CREATE TRIGGER update_user_age AFTER UPDATE ON users \
        BEGIN \
        SELECT onTrigger('b', age);\
        END;";

    const char *sSQL6 = "update users set age = 10 where userid = \'wang\'";

    sqlite3 *db = 0;
    char *pErrMsg = 0;
    int ret = 0;


    //连接数据库
    if (argc == 2)
        ret = sqlite3_open(argv[1], &db);
    else
        ret = sqlite3_open("./test.db", &db);

    sqlite3_create_function(db, "firstchar", 1, SQLITE_UTF8, NULL, &firstchar, NULL, NULL);
    sqlite3_create_function(db, "onTrigger", 2, SQLITE_UTF8, NULL, &onTrigger, NULL, NULL);
    if (ret != SQLITE_OK)
    {
        fprintf(stderr, "无法打开数据库：%s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        return 1;
    }
    printf("数据库连接成功\n");

    //执行建表SQL
    ret = sqlite3_exec(db, sSQL1, _sql_callback, 0, &pErrMsg);
    if (ret != SQLITE_OK)
    {
        fprintf(stderr, "SQL create error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg); //这个要的哦，要不然会内存泄露的哦！！！
        sqlite3_close(db);
        return 1;
    }
    printf("数据库建表成功！！\n");

    //执行插入数据
    ret = sqlite3_exec(db, sSQL2, _sql_callback, 0, &pErrMsg);
    if (ret != SQLITE_OK)
    {
        fprintf(stderr, "SQL insert error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg); //这个要的哦，要不然会内存泄露的哦！！！
        sqlite3_close(db);
        return 1;
    }
    printf("数据库插入数据成功！\n");

    //执行查询操作
    ret = sqlite3_exec(db, sSQL3, _sql_callback, 0, &pErrMsg);
    if (ret != SQLITE_OK)
    {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return 1;
    }
    printf("数据库查询成功！！\n");

    //执行用户自定义函数操作
    ret = sqlite3_exec(db, sSQL4, _sql_callback, 0, &pErrMsg);
    if (ret != SQLITE_OK)
    {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return 1;
    }
    printf("数据库自定义操作函数执行成功！！\n");

    //触发器操作
    ret = sqlite3_exec(db, sSQL5, _sql_callback, 0, &pErrMsg);
    if (ret != SQLITE_OK)
    {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return 1;
    }
    printf("-->%d\n", sqlite3_exec(db, sSQL1_2, _sql_callback, 0, &pErrMsg));
    printf("-->%d\n", sqlite3_exec(db, sSQL2_2, _sql_callback, 0, &pErrMsg));
    printf("-->%d\n", sqlite3_exec(db, sSQL6, _sql_callback, 0, &pErrMsg));
    printf("触发器操作成功！！\n");


    //关闭数据库
    sqlite3_close(db);
    db = 0;
    return 0;
}
