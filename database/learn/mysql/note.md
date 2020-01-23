## 数据库表描述

    select column_name,column_comment,data_type,column_type from information_schema.columns where table_name='table'

## 格式化显示数据表

    select * from db.table limit 1\G
