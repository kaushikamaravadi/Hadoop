### Problem 1 

given a tsv file, extract first 7 columns and write back to hdfs 

df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))

sc.parallelize(df.takeSample(False,7)).saveAsTextFile('/user/kaushik/pyspark/takesevenseven.txt')

sc.parallelize(df.take(7)).saveAsTextFile('/user/kaushik/pyspark/takeseven1st.txt')

data = df.toDF()

data.select('_1').show()

dd = data.select('_1','_2','_3','_4','_5').take(7)

>>> df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t')).map(lambda l:(l[0],l[1]))
>>> df.first()
(u'1', u'1')


### Problem 2

>>> df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))
>>> data = df.toDF()
>>> data.write.parquet('/user/kaushik/cca/test1.parquet')


### Problem 3

avro-tools getschema first.avro > ./first.avsc

### Problem 4

parquet snappy
BY DEFAULT GZIP COMPRESSED

>>> df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))

> sqlContext.setConf("spark.sql.parquet.compression.codec.", "codec")

>>> dd = sqlContext.createDataFrame(df,['u','m','r','j','t'])
>>> dd.write.parquet('/user/kaushik/cca/')

sqlContext.setConf("spark.sql.parquet.compression.codec.", "snappy")
>>> dd = sqlContext.createDataFrame(df,['u','m','r','j','t'])
>>> dd.write.parquet('/user/kaushik/cca/par')

dd.write.option("compression","lzo").save('/user/kaushik/cca/gzip000')

spark.sql.parquet.compression.codec	gzip	Sets the compression codec use when writing Parquet files. Acceptable values include: uncompressed, snappy, gzip, lzo
### Problem 4


dd.write.option("compression","none").save('/user/kaushik/pyspark/gzip1000')



