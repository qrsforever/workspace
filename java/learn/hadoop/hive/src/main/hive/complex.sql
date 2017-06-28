-- 设置打印列名
set hive.cli.print.header=true;

drop table if exists login_array;

-- ================================数组
create table login_array(
    ip string,
    uids array<BIGINT>
)
partitioned by (dt string)
row format delimited 
fields terminated by ','
collection items terminated by '|'
stored as textfile;

-- 导入数据
load data local inpath 'tmp/login_array.txt'
overwrite into table login_array
partition(dt='20170620');

-- 查询数组[0], 计算数组长度(别名len)
select ip, uids[0], size(uids) as len from login_array
where dt='20170620';

-- 数组中包含查询
select ip from login_array
where array_contains(uids,3105007005);

-- 显示metadata
dfs -cat /user/lidong/warehouse/login_array/dt=20170620/login_array.txt;

drop table if exists login_map;

-- ==============================map集合
create table login_map(
    ip string,
    users map<string, bigint>
)
partitioned by (dt string)
row format delimited 
fields terminated by ','
collection items terminated by '|'
map keys terminated by ':'
stored as textfile;

load data local inpath 'tmp/login_map.txt'
overwrite into table login_map 
partition(dt='20170621');

-- 查询
select ip, size(users) as maplen from login_map
where dt='20170621';

-- 包含查询
select ip, users['aa'] as keyaa from login_map
where array_contains(map_keys(users), 'aa');

drop table if exists login_struct;

-- ==============================struct
create table login_struct (
    ip string,
    users struct<name:string, uid:bigint>
)
row format delimited
fields terminated by ','
collection items terminated by ':'
stored as textfile;

load data local inpath 'tmp/login_struct.txt'
overwrite into table login_struct;

select ip, users from login_struct;
select ip, users.name from login_struct;

drop table if exists login_complex;

-- ==============================complext(array-struct)
create table login_complex (
    ip string,
    users array<struct<name:string, uid:bigint>>
)
row format delimited
fields terminated by ','
collection items terminated by '|'
map keys terminated by ':'
stored as textfile;

load data local inpath 'tmp/login_complex.txt'
overwrite into table login_complex;

select ip, users[0], size(users) from login_complex;
