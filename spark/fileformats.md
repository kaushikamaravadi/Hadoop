### convert tsv file to avro and save in hdfs 

df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))
votedf = df.toDF()
votedf.write.format('com.databricks.spark.avro').save('/user/kaushik/pyspark/avrofile')


### read avro file 

readvote = sqlContext.read.format('com.databricks.spark.avro').load('/user/kaushik/pyspark/avrofile/first.avro')

### Read Json file 

>>> df = sqlContext.read.json('/user/kaushik/depts.json')
>>> df.first()
Row(department_id=2, department_name=u'Fitness')

### Write Json to HDFS

>>> df
DataFrame[department_id: bigint, department_name: string]
>>> df.write.json('/user/kaushik/pyspark/cca/test.json')



### Write Parquet files to HDFS

df.toDF()

df.write.parquet('/user/kaushik/cca/test.parquet')

### Read Parquet File 

df = sqlContext.read.parquet('/user/kaushik/cca/test.parquet')

### avro to csv 

>>> iris = sqlContext.read.format('com.databricks.spark.csv').load('/user/kaushik/iris.csv')
>>> iris.count()
150
>>> iris.write.format('csv').save('/user/kaushik/pyspark/csh')
>>> readvote = sqlContext.read.format('com.databricks.spark.avro').load('/user/kaushik/pyspark/avrofile/first.avro')
>>> readvote.write.format('csv').save('/user/kaushik/pyspark/chennai')
>>> iris.write.format('com.databricks.spark.avro').save('/user/kaushik/pyspark/cshavro')


### pure tsv


CREATE TEMPORARY TABLE episodes
USING com.databricks.spark.avro
OPTIONS (path "src/test/resources/episodes.avro")

### temptable
sqlContext.registerDataFrameAsTable(df, "table1")


