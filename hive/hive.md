```sql

CREATE DATABASE ebay;
```
```sql

CREATE TABLE ebay.auction(openingBid INT, finalBid INT, itemType STRING, days INT);
LOAD DATA INPATH '/user/kaushik/auctiondata.csv' INTO TABLE ebay.auction;
```
```sql

CREATE DATABASE kaushik_santosh14 LOCATION '/user/kaushik_santosh14/hive/kaushik_santosh';
```
```sql

DROP DATABASE IF EXISTS sk CASCADE;
```
### Create table employee (database= kaushik_santosh14)

```sql

CREATE TABLE if NOT EXISTS kaushik_santosh14.employee (eid int,name STRING, salary INT, destination STRING)
COMMENT 'employee details'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
```
### load data from test.csv into employee table

```sql

LOAD DATA INPATH '/user/kaushik/test.csv' OVERWRITE INTO TABLE kaushik_santosh14.employee;
```

```
LOCAL is identifier to specify the local path. It is optional.
OVERWRITE is optional to overwrite the data in the table.
PARTITION is optional.
```

```sql
CREATE TABLE if NOT EXISTS kaushik_santosh14.employee (station STRING, latitude INT,longitude INT)
COMMENT 'employee details'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
LOAD DATA INPATH '/user/kaushik_santosh14/auctiondata.csv' OVERWRITE INTO TABLE kaushik_santosh14.employee;
```

```sql

ALTER TABLE kaushik_santosh14.employee rename to kaushik_santosh14.emp;
ALTER TABLE kaushik_santosh14.emp ADD COLUMNS (nexus int COMMENT 'tested alter command'); 
ALTER table kaushik_santosh14.emp CHANGE salary Salaries STRING;
ALTER TABLE kaushik_santosh14.emp REPLACE COLUMNS(eid INT empid int);
```

## RELATIONAL OPERATORS

```sql
select employee.station,employee.latitude from kaushik_santosh14.employee where employee.latitude > 70;
```
```sql

select employee.station,employee.latitude from kaushik_santosh14.employee where employee.latitude > 70;
```
```sql

SELECT employee.station,employee.latitude FROM kaushik_santosh14.employee WHERE employee.latitude = 90;
```
```sql

select employee.station from kaushik_santosh14.employee where employee.station = 'Clean_Air' and employee.latitude = 90;
```

## CREATE A TITANIC TABLE IN KAUSHIK_SANTOSH14 DATABASE AND SAVE IT AS TEXT FILE FIELDS SEPERATED BY ',' AND LINES TERMINATED BY '\n' AND LOAD TRAIN.CSV FILE INTO TABLE

```sql

CREATE TABLE if NOT EXISTS kaushik_santosh14.titanic 
(passengerid int,survived INT, pclass INT, 
name VARCHAR(300),sex STRING,age FLOAT,siblings INT,parch INT,
ticket VARCHAR(100),fare FLOAT,cabin VARCHAR(100), embarked STRING)
COMMENT 'titanic'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
LOAD DATA INPATH '/user/kaushik/train.csv' OVERWRITE INTO TABLE kaushik_santosh14.titanic;
```

```sql

select titanic.name from kaushik_santosh14.titanic where titanic.survived = 1 and titanic.pclass = 3;
```
```sql

select count(titanic.survived) from kaushik_santosh14.titanic where titanic.survived =0;
```
## CREATE DATSET DATABASE AND STORE IT IN AVRO FORMAT

```sql
create table iris.iris_data
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
tblproperties ('avro.schema.literal'='{
"name": "my_record",
"type": "record",
"fields": [
{"name":"s_length", "type":"int"},
{"name":"s_width", "type":"int"},
{"name":"p_length", "type":"int"},
{"name":"p_width", "type":"int"},
{"name":"species", "type":"string"}
]}');
```


```sql
create table iris.iris_table1(s_length INT,s_width INT,p_length INT,p_width INT,species STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' stored as textfile;
```
```sql
load data inpath '/user/kaushik/iris.csv' overwrite into table iris.iris_table1;
select * from iris.iris_table1;
select avg(s_length) from iris.iris_table1;
```
```sql
create table iris.iris_data1
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
tblproperties ('avro.schema.literal'='{
"name": "my_record",
"type": "record",
"fields": [
{"name":"s_length", "type":["int","null"],"default":0},
{"name":"s_width", "type":["int","null"],"default":0},
{"name":"p_length", "type":["int","null"],"default":0},
{"name":"p_width", "type":["int","null"],"default":0},
{"name":"species", "type":["string","null"],"default":null}
]}');

insert overwrite table iris.iris_data1 select * from iris.iris_table1;
select avg(s_length) from iris.iris_data1;
```

