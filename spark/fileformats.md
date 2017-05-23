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

 = 
### Write Json to HDFS

>>> df
DataFrame[department_id: bigint, department_name: string]
>>> df.write.json('/user/kaushik/pyspark/cca/test.json')



### Write Parquet files to HDFS

df.toDF()

df.write.parquet('/user/kaushik/cca/test.parquet')

### Read Parquet File 

df = sqlContext.read.parquet('/user/kaushik/cca/test.parquet')



CREATE TEMPORARY TABLE episodes
USING com.databricks.spark.avro
OPTIONS (path "src/test/resources/episodes.avro")


sqlContext.registerDataFrameAsTable(df, "table1")

sqlContext = SQLContext(sc)
schema = StructType([StructField("user_id", FloatType()),
    StructField("movie_id", FloatType()),
    StructField("rating", FloatType()),
    StructField("junk", FloatType()),
    StructField("timestamp", StringType())
])

