drop table if exists records;

create table records (year string, temperature int, quality int) 
row format delimited fields terminated by '\t';

show tables;

-- overwrite 如果文件已经存在删除
load data local inpath '../guide/input/ncdc/micro-tab/sample.txt' 
overwrite into table records;

select * from records;

-- 将查询转化为Job， 先分组再求最大温度max
select year, max(temperature) from records
where temperature != 9999 and quality in (0, 1, 4, 5, 9) 
group by year;
