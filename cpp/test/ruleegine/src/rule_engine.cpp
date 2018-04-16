#include <stdio.h>
#include <sqlite3.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>

#include <libxml/parser.h>
#include <libxml/tree.h>

#define DB_PATH "/tmp/iot.db"
#define XML_PATH "res/rules.xml"

#define CREATE_TABLE_TH "create table product_8GBCH2FO2(\
    dname varchar(32), \
    temp int, \
    humi int, \
    date datetime);"

#define CREATE_TABLE_AC "create table product_S7JV8369SF(\
    dname varchar(32) , \
    power int);"

#define CREATE_TRIGGER_FOR_TH "create trigger %s \
    after update of %s on product_%s \
    when new.dname = '%s' and %s \
    begin \
    select on_trigger_cb( \
        'product_%s', \
        '%s', \
        '%s');\
    end "

#define INSERT_TABLE_DEFAULT_TH "insert into product_8GBCH2FO2 \
    values('testTH1', 10, 10, '2018-04-14');"

#define INSERT_TABLE_DEFAULT_AC "insert into product_S7JV8369SF \
    values('testAC1', 0);"

#define UPDATE_TABLE_TH "update product_8GBCH2FO2 \
    set temp = 40 where dname = 'testTH1'"

#define SELECT_TABLE_AC "SELECT * from product_S7JV8369SF"

static int _sql_exec_callback(void *notused, int argc, char **argv, char **szColName)
{
    int i = 0;
    printf("notused:%p, argc:%d\n", notused, argc);
    for (i = 0; i < argc; i++)
        printf("%s = %s\n", szColName[i], argv[i] == 0 ? "NULL" : argv[i]);
    printf("\n");
    return 0;
}

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

static void on_trigger_cb(sqlite3_context *context, int argc, sqlite3_value **argv)
{
    if (argc != 3)
        return;
    printf("on_trigger_cb argc = %d\n", argc);

    if(sqlite3_value_type(argv[0]) != SQLITE_TEXT)
        return;

    if(sqlite3_value_type(argv[1]) != SQLITE_TEXT)
        return;

    if(sqlite3_value_type(argv[2]) != SQLITE_TEXT)
        return;
    const char *productKey = (const char*)sqlite3_value_text(argv[0]);
    const char *deviceName = (const char*)sqlite3_value_text(argv[1]);
    const char *parameters = (const char*)sqlite3_value_text(argv[2]);
    printf("productKey[%s] deviceName[%s] parameters[%s]\n", productKey, deviceName, parameters);
}

int main(int argc, char *argv[])
{
    sqlite3 *db = 0;
    char *pErrMsg = 0;
    int ret = 0;

    xmlDocPtr doc;
    xmlNodePtr curNode;
    xmlChar *szKey;
    char buff[1024] = { 0 };

    if (SQLITE_OK != sqlite3_open(DB_PATH, &db)) {
        fprintf(stderr, "Open db[%s] error:%s\n", DB_PATH, sqlite3_errmsg(db));
        return -1;
    }

    sqlite3_create_function(db, "on_trigger_cb", 3, SQLITE_UTF8, NULL, &on_trigger_cb, NULL, NULL);

    printf("Create table th: %s\n", CREATE_TABLE_TH);
    ret = sqlite3_exec(db, CREATE_TABLE_TH, 0, 0, &pErrMsg);
    if (ret != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return -1;
    }
    printf("ok\n");

    printf("Create table ac: %s\n", CREATE_TABLE_AC);
    ret = sqlite3_exec(db, CREATE_TABLE_AC, 0, 0, &pErrMsg);
    if (ret != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return -1;
    }
    printf("ok\n");

    doc = xmlReadFile(XML_PATH, "GB2312", XML_PARSE_RECOVER);
    if (0 == doc) {
        fprintf(stderr, "xmlReadFile[%s] error!\n", XML_PATH);
        return -1;
    }

    curNode = xmlDocGetRootElement(doc);
    if (NULL == curNode) {
        fprintf(stderr,"empty document");
        xmlFreeDoc(doc);
        return -1;
    }
    if (xmlStrcmp(curNode->name, BAD_CAST "root")) {
        fprintf(stderr,"document of the wrong type, root node != root");
        xmlFreeDoc(doc);
        return -1;
    }

    xmlNodePtr rootPtr = curNode->xmlChildrenNode;
    while (rootPtr != NULL) {
        char rulename[64] = { 0 };
        char fields[32] = { 0 };
        char from[64] = { 0 };
        char to[64] = { 0 };
        char productID1[16] = { 0 };
        char productID2[16] = { 0 };
        char dname1[32] = { 0 };
        char dname2[32] = { 0 };
        char params[128] = { 0 };
        char condition[128] = { 0 };
        /* parse rule */
        if ((!xmlStrcmp(rootPtr->name, (const xmlChar *)"rule"))) {
            szKey = xmlGetProp(rootPtr, BAD_CAST "name");
            if (0 == szKey)
                continue;
            strcpy(rulename, (const char*)szKey);
            xmlFree(szKey);

            xmlNodePtr rulePtr = rootPtr->xmlChildrenNode;
            while (rulePtr != NULL) {
                /* parse event */
                if ((!xmlStrcmp(rulePtr->name, (const xmlChar *)"event"))) {
                    xmlNodePtr eventPtr = rulePtr->xmlChildrenNode;
                    while (eventPtr != NULL) {
                        if (!xmlStrcmp(eventPtr->name, (const xmlChar *)"fields")) {
                            szKey = xmlNodeGetContent(eventPtr);
                            // printf("\n%s:%s\n", eventPtr->name, szKey);
                            strcpy(fields, (const char*)szKey);
                            xmlFree(szKey);
                        }
                        if (!xmlStrcmp(eventPtr->name, (const xmlChar *)"from")) {
                            szKey = xmlNodeGetContent(eventPtr);
                            // printf("\n%s:%s\n", eventPtr->name, szKey);
                            strcpy(from, (const char*)szKey);
                            sscanf(from, "%[^/]/%[^/]/%*s", productID1, dname1);
                            xmlFree(szKey);
                        }
                        if (!xmlStrcmp(eventPtr->name, (const xmlChar *)"condition")) {
                            szKey = xmlNodeGetContent(eventPtr);
                            // printf("\n%s:%s\n", eventPtr->name, szKey);
                            char word[64] = { 0 };
                            char *tt = (char*)szKey;
                            char *ss = word;
                            do {
                                *ss = *tt++;
                                if ((*ss == ' ' || *tt =='\0') && strlen(word) > 0) {
                                    if (*ss == ' ')
                                        *ss = 0;
                                    int numflg = 1;
                                    char *t = word;
                                    while (*t != '\0') {
                                        if (!isdigit(*t) && *t != '.') {
                                            numflg = 0;
                                            break;
                                        }
                                        t++;
                                    }
                                    if (numflg || !strcmp(word, ">") || !strcmp(word, "<") ||
                                        !strcmp(word, ">=") || !strcmp(word, "<=") ||
                                        !strcmp(word, "=") || !strcasecmp(word, "in") ||
                                        !strcasecmp(word, "and") || !strcasecmp(word, "or") ||
                                        !strcasecmp(word, "like")) {
                                        strcat(condition, " ");
                                    } else {
                                        strcat(condition, " new.");
                                    }
                                    strcat(condition, word);
                                    memset(word, 0, sizeof(word));
                                    ss = word;
                                    continue;
                                }
                                ss++;
                            } while (*tt);
                            xmlFree(szKey);
                        }
                        eventPtr = eventPtr->next;
                    }
                } else if ((!xmlStrcmp(rulePtr->name, (const xmlChar *)"control"))) {
                    /* parse control */
                    xmlNodePtr controlPtr = rulePtr->xmlChildrenNode;
                    while (controlPtr != NULL) {
                        if (!xmlStrcmp(controlPtr->name, (const xmlChar *)"to")) {
                            szKey = xmlNodeGetContent(controlPtr);
                            // printf("\n%s:%s\n", controlPtr->name, szKey);
                            strcpy(to, (const char*)szKey);
                            sscanf(to, "%[^/]/%[^/]/%*s", productID2, dname2);
                            xmlFree(szKey);
                        } else if (!xmlStrcmp(controlPtr->name, (const xmlChar *)"data")) {
                            szKey = xmlNodeGetContent(controlPtr);
                            // printf("\n%s:%s\n", controlPtr->name, szKey);
                            strcpy(params, (const char*)szKey);
                            xmlFree(szKey);
                        }
                        controlPtr = controlPtr->next;
                    }
                }
                rulePtr = rulePtr->next;
            }
            /* add rule to sql */
            printf("%s, %s, %s, %s, %s, %s, %s, %s\n", rulename, fields, productID1, dname1, condition, productID2, dname2, params);
            if (rulename[0] && fields[0] && productID1[0] && dname1[0] && condition[0] && productID2[0] && dname2[0] && params[0]) {
                snprintf(buff, 1023, CREATE_TRIGGER_FOR_TH,
                    rulename, fields, productID1, dname1, condition, productID2, dname2, params);
                // printf("Create trigger: %s\n", buff);
                ret = sqlite3_exec(db, buff, 0, 0, &pErrMsg);
                if (ret != SQLITE_OK) {
                    fprintf(stderr, "SQL error: %s\n", pErrMsg);
                    sqlite3_free(pErrMsg);
                    sqlite3_close(db);
                    return -1;
                    printf("ok\n");
                }
            }
        }
        rootPtr = rootPtr->next;
    }

    printf("insert default th: %s\n", INSERT_TABLE_DEFAULT_TH);
    ret = sqlite3_exec(db, INSERT_TABLE_DEFAULT_TH, 0, 0, &pErrMsg);
    if (ret != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return -1;
    }
    printf("ok\n");

    printf("insert default ac: %s\n", INSERT_TABLE_DEFAULT_AC);
    ret = sqlite3_exec(db, INSERT_TABLE_DEFAULT_AC, 0, 0, &pErrMsg);
    if (ret != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return -1;
    }
    printf("ok\n");

    printf("update table th: %s\n", UPDATE_TABLE_TH);
    ret = sqlite3_exec(db, UPDATE_TABLE_TH, _sql_exec_callback, (void*)UPDATE_TABLE_TH, &pErrMsg);
    if (ret != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return -1;
    }
    printf("ok\n");

    printf("select table ac: %s\n", SELECT_TABLE_AC);
    ret = sqlite3_exec(db, SELECT_TABLE_AC, _sql_exec_callback, (void*)SELECT_TABLE_AC, &pErrMsg);
    if (ret != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\n", pErrMsg);
        sqlite3_free(pErrMsg);
        sqlite3_close(db);
        return -1;
    }
    printf("ok\n");

    sqlite3_close(db);
    db = 0;
    return 0;
}
