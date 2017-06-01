### Problem 1 

```python 

df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))
```
```python
sc.parallelize(df.takeSample(False,7)).saveAsTextFile('/user/kaushik/pyspark/takesevenseven.txt')
```
```python
sc.parallelize(df.take(7)).saveAsTextFile('/user/kaushik/pyspark/takeseven1st.txt')
```
```python
data = df.toDF()
```
```python
data.select('_1').show()
```
```python
dd = data.select('_1','_2','_3','_4','_5').take(7)
```
```python
df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t')).map(lambda l:(l[0],l[1]))
```
```python
df.first()
```
(u'1', u'1')


### Problem 2
```python
df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))
```
```python
data = df.toDF()
```
```python
data.write.parquet('/user/kaushik/cca/test1.parquet')
```

### Problem 3

```python

df = sc.textFile('/user/kaushik/iris.csv').map(lambda l: l.split(','))
```
```python
df.count()
```

151
```python
from pyspark.sql.types import *
```
```python
schema = StructType([StructField("sep_len", DecimalType()),
...     StructField("sep_wid", DecimalType()),
...     StructField("pet_len", DecimalType()),
...     StructField("pet_wid", DecimalType()),
...     StructField("species", StringType())
... ])
```
```python
dd = sqlContext.createDataFrame(df, schema)
```

DataFrame[sep_len: float, sep_wid: float, pet_len: float, pet_wid: float, species: string]



### Problem 4

parquet snappy
BY DEFAULT GZIP COMPRESSED
```python
df = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t'))
```
```python
sqlContext.setConf("spark.sql.parquet.compression.codec.", "codec")
```
```python
sqlContext.setConf("spark.sql.avro.compression.codec","codec") 
```
```python
sqlContext.setConf("spark.sql.avro.deflate.level", "5")
```
```python
dd = sqlContext.createDataFrame(df,['u','m','r','j','t'])
```
```python
dd.write.parquet('/user/kaushik/cca/')
```
```python
sqlContext.setConf("spark.sql.parquet.compression.codec.", "snappy")
```
```python
dd = sqlContext.createDataFrame(df,['u','m','r','j','t'])
```
```python
dd.write.parquet('/user/kaushik/cca/par')
```
```python
dd.write.option("compression","lzo").save('/user/kaushik/cca/gzip000')
```

### spark.sql.parquet.compression.codec	gzip	Sets the compression codec use when writing Parquet files. Acceptable values include: uncompressed, snappy, gzip, lzo

### Problem 4

```python
dd.write.option("compression","none").save('/user/kaushik/pyspark/gzip1000')
```


