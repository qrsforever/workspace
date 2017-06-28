-- 设置打印列名
set hive.cli.print.header=true;

drop table if exists login;

-- 这个表并存在mysql中， mysql只是存了信息
-- 建立多区表(双分区)
create table login (
    uid bigint,
    ip string
)
partitioned by (dt string comment 'date', hr string comment 'hour')
row format delimited 
fields terminated by ','
stored as textfile;

-- 向分区导入数据, 只是复制数据到dfs对应的列目录中
load data local inpath "tmp/login.txt"
overwrite into table login 
partition (dt='20170628', hr='20');

-- 添加分区
alter table login add 
partition(dt='20170629', hr='07')
partition(dt='20170629', hr='08');

load data local inpath "tmp/login2.txt"
overwrite into table login 
partition (dt='20170629', hr='07');

-- 显示分区
show partitions login;

-- 显示dfs存储目录结构
dfs -ls /user/lidong/warehouse/login;

-- 输出dfs存储的数据
dfs -cat /user/lidong/warehouse/login/dt=20170629/hr=07/login2.txt;

-- 显示指定分区的内容
select * from login where login.dt>='20170629';

-- 删除一个分区
alter table login drop partition(dt='20170629', hr='07');
show partitions login;
