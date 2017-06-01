## All variables are Dataframes 

### convert tsv file to avro and save in hdfs 

```python
df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))
```
```python
votedf = df.toDF()
```
```python
votedf.write.format('com.databricks.spark.avro').save('/user/kaushik/pyspark/avrofile')
```

### Read Avro file 

```python
readvote = sqlContext.read.format('com.databricks.spark.avro').load('/user/kaushik/pyspark/avrofile/first.avro')
```

### Write Avro

```python
writevote = sqlContext.read.format('com.databricks.spark.avro').load('/user/kaushik/pyspark/avrofile')
```

### Read Json file 

```python
df = sqlContext.read.json('/user/kaushik/depts.json')
```
```python
df.first()
```
Row(department_id=2, department_name=u'Fitness')

### Write Json to HDFS


DataFrame[department_id: bigint, department_name: string]
```python
df.write.json('/user/kaushik/pyspark/cca/test.json')
```


### Write Parquet files to HDFS

```python
df.toDF()
```
```python
df.write.parquet('/user/kaushik/cca/test.parquet')
```

### Read Parquet File 

```python
df = sqlContext.read.parquet('/user/kaushik/cca/test.parquet')
```
### avro to csv 

```python
readvote = sqlContext.read.format('com.databricks.spark.avro').load('/user/kaushik/pyspark/avrofile/first.avro')
```
```python
readvote.write.format('csv').save('/user/kaushik/pyspark/chennai')
```
```python
iris.write.format('com.databricks.spark.avro').save('/user/kaushik/pyspark/cshavro')
```

### SQL COMMAND

```sql
CREATE TEMPORARY TABLE episodes
USING com.databricks.spark.avro
OPTIONS (path "src/test/resources/episodes.avro")
```
### temptable

```python
sqlContext.registerDataFrameAsTable(df, "table1")
```


