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
```sql

CREATE TABLE if NOT EXISTS kaushik_santosh14.employee (eid int,name STRING, salary INT, destination STRING)
COMMENT 'employee details'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
```
```sql

LOAD DATA INPATH '/user/kaushik/test.csv' OVERWRITE INTO TABLE kaushik_santosh14.employee;
```

LOCAL is identifier to specify the local path. It is optional.
OVERWRITE is optional to overwrite the data in the table.
PARTITION is optional.


CREATE TABLE if NOT EXISTS kaushik_santosh14.employee (station STRING, latitude INT,longitude INT)
COMMENT 'employee details'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
LOAD DATA INPATH '/user/kaushik_santosh14/auctiondata.csv' OVERWRITE INTO TABLE kaushik_santosh14.employee;


ALTER TABLE kaushik_santosh14.employee rename to kaushik_santosh14.emp;
ALTER TABLE kaushik_santosh14.emp ADD COLUMNS (nexus int COMMENT 'tested alter command'); 
ALTER table kaushik_santosh14.emp CHANGE salary Salaries STRING;
ALTER TABLE kaushik_santosh14.emp REPLACE COLUMNS(eid INT empid int);

## RELATIONAL OPERATORS
select employee.station,employee.latitude from kaushik_santosh14.employee where employee.latitude > 70;
-- select employee.station,employee.latitude from kaushik_santosh14.employee where employee.latitude > 70;
-- SELECT employee.station,employee.latitude FROM kaushik_santosh14.employee WHERE employee.latitude = 90;
select employee.station from kaushik_santosh14.employee where employee.station = 'Clean_Air' and employee.latitude = 90;




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


-- select titanic.name from kaushik_santosh14.titanic where titanic.survived = 1 and titanic.pclass = 3;
select count(titanic.survived) from kaushik_santosh14.titanic where titanic.survived =0;

