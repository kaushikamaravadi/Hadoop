## Sqoop

Apache Sqoop is a tool designed for efficiently transferring bulk data between Apache Hadoop and external datastores
 such as relational databases, enterprise data warehouses.

### CREATE DATABASE

create database cloudera_test;

### CREATE TABLES

create table cloudera_test.test(id int, name varchar(10),contact int);
create table cloudera_test.test1(id int, name varchar(10),contact int);

### INSERT DATA INTO TABLES

insert into cloudera_test.test(id,name,contact) values (12,"john",100);
insert into cloudera_test.test1 (user_id, user_name,user_address, user_contact) values (143,"mark","us", 10013);

### GRANT PREVILEGES

grant all privileges on cloudera_test.* to 'root'@'localhost';
flush privilages;


## SQOOP COMMANDS

### LIST ALL DATABASES in localhost

sqoop list-databases --connect "jdbc:mysql://localhost/cloudera_test" --username=root --password=ubuntu@kaushik

### IMPORT TABLE test 

sqoop import --connect jdbc:mysql://localhost/cloudera_test --username root --password namenode --table test -m 1 --target-dir '/user/kaushik/directory'

### LIST ALL DATABASES in 35.184.147.216

sqoop list-databases --connect "jdbc:mysql://35.184.147.216/" --username=root --password=iamgroot

### FIELDS TERMINATED BY '|' , only one mapper , target-dir 

sqoop import --connect "jdbc:mysql://35.184.147.216/univ" --username=root --password=iamgroot --table takes --fields-terminated-by '\' -m 1 --target-dir '/user/directory'

### Columns

sqoop import --connect "jdbc:mysql://35.184.147.216/mysql" --username=root --password=iamgroot --table user --columns 'Host' 

### LIST ALL DATABASES 

sqoop list-databases --connect "jdbc:mysql://35.184.147.216/" --username=root --password=iamgroot

### IMPORT ndh TABLE FROM sqoopPractice using one mapper and target-dir

sqoop import --connect "jdbc:mysql://35.184.147.216/sqoopPractice" --username=root --password=iamgroot --table ndh -m 1 --target-dir '/user/kaushik/import/Host/yesh'

### IMPORT-ALL-TABLES

sqoop import-all-tables --connect "jdbc:mysql://35.184.147.216/mysql" --username=root --password=iamgroot -m 1

### QUERY

sqoop eval --connect "jdbc:mysql://35.184.147.216/univ" --username=root --password=iamgroot --query "SELECT * FROM takes limit 5"

```
localhost= 35.184.147.216
password= iamgroot
```

### IMPORTING QUERY

sqoop import --connect "jdbc:mysql://35.184.147.216/univ" --username=root --password=iamgroot --query "SELECT * FROM takes where \$CONDITIONS" --target-dir '/user/eval_import' -m 1

### WHERE

sqoop import --connect "jdbc:mysql://35.184.147.216/univ" --username=root --password=iamgroot --query "SELECT * FROM takes where course_id=239 and \$CONDITIONS"  --target-dir '/user/eval_import/my_import' -m 1

### as-avrodatafile

sqoop import --connect "jdbc:mysql://35.184.147.216/univ" --username=root --password=iamgroot --query "SELECT * FROM takes where course_id=239 and \$CONDITIONS"  --target-dir '/user/eval_import/my_import_avro' -m 1 --as-avrodatafile

###  Create hive table

sqoop import-table --connect "jdbc:mysql://35.184.147.216/univ" --username=root --password=iamgroot -m 1 --table ndh --hive-import --create-hive-table

### sqoop job

sqoop job --create first -- import --connect jdbc:mysql://35.184.147.216/univ --username root --password iamgroot --table ndh -m 1 --target-dir /user/sqoop_job --incremental append --check-column course_id

sqoop job --show first

sqoop job --list

### COMPRESS

sqoop import --connect "jdbc:mysql://35.184.147.216/univ" --username=root --password=iamgroot --table takes --fields-terminated-by '\' --compress --compression-codec org.apache.hadoop.io.compress.SnappyCodec -m 1 --target-dir '/user/directory/compress'



