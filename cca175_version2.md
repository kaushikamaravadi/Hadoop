# CCA 175


## Data Ingest


### Import data from a MySQL database into HDFS using Sqoop

```sh

sqoop import --connect jdbc:mysql//localhost/pyspark --username root --password Srianjaneyam@34 --table customer -m 1 --target-dir /user/kaushik_amaravadi/customer_table
```
```sh
sqoop import --connect jdbc:mysql://localhost/pyspark --username root --password Kaushik123@ --table orderss -m 1 --fields-terminated-by '\t' --target-dir /user/kaushik_amaravadi/order_tsv --as-textfile
```

```sh
sqoop import --connect jdbc:mysql://localhost/pyspark --username root --password Kaushik1
23@ --table customer -m 1 --fields-terminated-by '\t' --target-dir /user/kaushik_amaravadi/customer_avro_snappy --as-avrodatafile --compress --compression-codec org.apache.hadoop.io.compress.SnappyCodec
```

### Export data to a MySQL database from HDFS using Sqoop

```sh

sqoop export --connect jdbc:mysql://localhost/pyspark --username root --password Srianjaneyam@34 --table customer -m 1 --export-dir /user/kaushik/customer_table 
```

```sh
sqoop export --connect jdbc:mysql://localhost/pyspark --username root --password Kaushik1
23@ --table orderss -m 1 --fields-terminated-by '\t' --export-dir /user/kaushik_amaravadi/order_tsv
```



### Change the delimiter and file format of data during import using Sqoop

```sh

sqoop import --connect jdbc:mysql://localhost/pyspark --username root --password Srianjaneyam@34 --table customer -m 1 --fields-terminated-by '\t' --lines-terminated-by '\n' --target-dir /user/kaushik_amaravadi/

sqoop export --connect jdbc:mysql://localhost/pyspark --username root --password Kaush
ik123@ --table customer -m 1 --input-fields-terminated-by '\t' --export-dir /user/kaushik_amaravadi/there

sqoop import --connect jdbc:mysql://localhost/pyspark --username root --password Kaush
ik123@ --table customer -m 1 --target-dir /user/kaushik_amaravadi/there --fields-terminated-by '\t' --as-textfile

### Ingest real-time and near-real-time streaming data into HDFS



### Process streaming data as it is loaded onto the cluster


### Load data into and out of HDFS using the Hadoop File System commands


## Transform, Stage, and Store

### Load RDD data from HDFS for use in Spark applications


### Write the results from an RDD back into HDFS using Spark


### Read and write files in a variety of file formats


### Perform standard extract, transform, load (ETL) processes on data


## Data Analysis

### Use metastore tables as an input source or an output sink for Spark applications


### Understand the fundamentals of querying datasets in Spark


### Filter data using Spark


### Write queries that calculate aggregate statistics


### Join disparate datasets using Spark


### Produce ranked or sorted data



