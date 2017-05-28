create database pyspark;

use pyspark;

create table pyspark.orderss (id int,amount int,primary key(id))
comment 'order details'
row format delimited
fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/kaushik/hive_database';


create table pyspark.customer (id int, first_name string,last_name string)
comment 'customer details'
row format delimited
fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/kaushik/hive_database';

insert into pyspark.orderss values(1,10);
insert into pyspark.orderss values(2,20);
insert into pyspark.orderss values(3,30);
insert into pyspark.orderss values(4,40);
insert into pyspark.orderss values(5,50);
insert into pyspark.orderss values(6,20);

insert into pyspark.customer values(1,'jayy','kanthgg');
insert into pyspark.customer values(2,'jayt','kanthh');
insert into pyspark.customer values(3,'jays','kanthy');
insert into pyspark.customer values(4,'jy','kan');
insert into pyspark.customer values(5,'jyt','anthh');
insert into pyspark.customer values(6,'ays','khy');


select * from pyspark.customer;
select * from pyspark.orderss;

drop table orderss;
