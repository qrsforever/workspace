-- ============ bucket: 细粒度的划分 (组距)

-- 作用: 1、提取数据样本 2、提高查询效率

drop table if exists bucket_tmp;

create table bucket_tmp (
    id int,
    age int,
    dt string
)
row format delimited fields terminated by ',';

load data local inpath 'tmp/login_bucket.txt'
overwrite into table bucket_tmp;

select * from bucket_tmp 
where age = 22;

drop table if exists stu_bucket;

-- 创建bucket表， 这里的sorted是针对每个bucket
create table stu_bucket(
    id int,
    age int
)
partitioned by (dt string)
clustered by(id) sorted by(age) into 10 buckets
row format delimited fields terminated by ',';

-- 这里的sort实际上没有必要， 和上面创建表的sort重， 有一个就可以
insert overwrite table stu_bucket 
partition(dt='20170620')
select id, age from bucket_tmp
where dt='20170620'
sort by age;

-- 查看dfs文件系统里面的对应的目录结构
dfs -ls /user/lidong/warehouse/stu_bucket/dt=20170620;
dfs -cat /user/lidong/warehouse/stu_bucket/dt=20170620/000006_0;

select * from stu_bucket limit 10;

-- 样本查询从10个buckets取出2(y=5)个, 从第2(x=2)个开始, 000001_0和000006_0
select * from stu_bucket tablesample(bucket 2 out of 5 on id);

-- 高效插入多个表， scan一次原表
drop table if exists insert_age_count;
create table insert_age_count(
    age int,
    cnt int
)
row format delimited fields terminated by ',';
drop table if exists insert_date_count;
create table insert_date_count(
    dt string,
    cnt int
)
row format delimited fields terminated by ',';

from bucket_tmp
insert overwrite table insert_age_count
    select age, count(age)
    group by age
insert overwrite table insert_date_count
    select dt, count(dt)
    group by dt;

-- 查看
hadoop fs -cat /user/lidong/warehouse/insert_age_count/000000_0
hadoop fs -cat /user/lidong/warehouse/insert_date_count/000000_0
