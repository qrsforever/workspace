# 常用命令

## 参考

    [官网手册](https://docs.mongodb.com/manual/mongo/)
    [mongodb的安装和配置](https://blog.csdn.net/zn505119020/article/details/81331808)
    [Python mogodb](http://www.runoob.com/python3/python-mongodb.html)

## 配置文件

    [更多](https://docs.mongodb.com/manual/reference/configuration-options/)

    `mongod -f /etc/mongod.conf`

    默认存储路径: `/data/db`

    进入后台管理: `mongo`

## 超级用户相关:

1. 进入数据库admin

    use admin

2. 增加或修改用户密码

    db.createUser({ user: "username", pwd: "password", roles: [{ role: "dbOwner", db: "yourdb" }] })

3. 查看用户列表

    db.system.users.find()

4. 用户认证

    db.auth('username','password')

5. 删除用户

    db.removeUser('name')

6. 查看所有用户

    show users

7. 查看所有数据库

    show dbs


## CRUD

### Create

```sql

use testdb

db.students.insert([
   { "_id" : 1,
      "grades" : [
        { type: "quiz", questions: [ 10, 8, 5 ] },
        { type: "quiz", questions: [ 8, 9, 6 ] },
        { type: "hw", questions: [ 5, 4, 3 ] },
        { type: "exam", questions: [ 25, 10, 23, 0 ] },

      ]
   }
])

show collections

```

### Read

```sql

db.students.find().pretty()

```

### Update

```sql

db.students.update(
   {},
   { $inc: { "grades.$[t].questions.$[score]": 2 } },
   { arrayFilters: [ { "t.type": "quiz" } , { "score": { $gte: 8 } } ], multi: true}
)

```

### Delete

```sql

db.dropDatabase()
db.students.drop()

```

## 导入/导出

[MongoDB导入导出以及数据库备份](https://www.cnblogs.com/qingtianyu2015/p/5968400.html)

如果value是嵌套的jason或者是数组, 使用csv不是很方便, 会转化为字符串

```sql

mongoexport -d testdb -c students --type json -o students_export1.json
mongoexport -d testdb -c students --type csv -f _id,grades -o students_export2.csv
mongoexport -d testdb -c students --type csv -f _id,grades --noHeaderLine -o students_export3.csv

mongoimport -d testdb -c students_import1 --type json --file students_export1.json
mongoimport -d testdb -c students_import2 --type csv --headerline --file students_export2.csv
mongoimport -d testdb -c students_import3 --type csv -f _id,grades --file students_export3.csv

show collections

```

## 备份/恢复

```sql

mongodump -h localhost:27017 -d testdb -o dump

mongorestore -h localhost:27017 -d testdb2 --dir dump/testdb

use testdb2
show collections

```
