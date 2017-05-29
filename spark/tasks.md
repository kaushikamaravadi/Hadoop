## Tasks

### Type Casting

irisrdd = sc.textFile('/user/kaushik/iris.csv').map(lambda l: l.split(',')).map(lambda l: (float(l[0]),float(l[1]),float(l[2]),float(l[3]),str(l[4])))

from pyspark.sql.types import *

schema = StructType([StructField("sep_len", FloatType(), True),
    StructField("sep_wid",FloatType(),True),
    StructField("pet_len",FloatType(),True),
    StructField("pet_wid",FloatType(), True),
    StructField("species", StringType(),True)
])

irisdf = sqlContext.createDataFrame(irisrdd,schema)

irisdf.show()

irisdf.write.parquet('/user/kaushik/tasks/iris/parquet_default')


### Task 1

voterdd = sc.textFile('/user/kaushik/Vote.txt').map(lambda l: l.split('\t')).map(lambda l: (float(l[0]), float(l[1]), float(l[2]), float(l[3])))

schema = StructType([StructField("user_id", FloatType()),
    StructField("movie_id", FloatType()),
    StructField("rating", FloatType()),
    StructField("junk", FloatType()), 
])

votedf = sqlContext.createDataFrame(voterdd, schema)

votedf
DataFrame[user_id: float, movie_id: float, rating: float, junk: float]

votedf.show()
+-------+--------+------+----+
|user_id|movie_id|rating|junk|
+-------+--------+------+----+
|    1.0|     1.0|   0.6| 1.0|
|    1.0|     2.0|   0.6| 1.0|
|    1.0|    10.0|   0.4| 1.0|
|    1.0|    13.0|   0.0| 0.2|
|    1.0|    17.0|   0.8| 1.0|
|    1.0|    18.0|   0.2| 1.0|
|    1.0|    19.0|   0.2| 1.0|
|    1.0|    21.0|   0.4| 1.0|
|    1.0|    25.0|   0.8| 1.0|
|    1.0|    31.0|   0.2| 1.0|
|    1.0|    32.0|   0.6| 1.0|
|    1.0|    34.0|   0.8| 1.0|
|    1.0|    36.0|   0.4| 1.0|
|    1.0|    39.0|   0.8| 1.0|
|    1.0|    41.0|   0.6| 1.0|
|    1.0|    43.0|   0.6| 1.0|
|    1.0|    44.0|   0.0| 0.2|
|    1.0|    45.0|   0.8| 1.0|
|    1.0|    47.0|   0.4| 1.0|
|    1.0|    50.0|   0.6| 1.0|
+-------+--------+------+----+
only showing top 20 rows

### With gzip compression which is default for parquet in spark 1.6.0

votedf.write.parquet('/user/kaushik/tasks/parquet_default')

### Without compression using option

votedf.write.option('compression','uncompressed').save('/user/kaushik/tasks/parquet_uncompressed')

### Options: uncompressed, snappy, gzip, lzo
### to set sqlContext

sqlContext.setConf("spark.sql.parquet.compression.codec.", "codec")

### parquet-tools

[kaushik_santosh14@namenode ~]$ hdfs dfs -copyToLocal /user/kaushik/tasks/parquet_default/part-r-00001-ce1558ca-dea5-489e-bfc0-35011f679252.gz.parquet /home/kaushik_santosh14
[kaushik_santosh14@namenode ~]$ parquet-tools schema part-r-00001-ce1558ca-dea5-489e-bfc0-35011f679252.gz.parquet
message spark_schema {
  optional float user_id;
  optional float movie_id;
  optional float rating;
  optional float junk;
}

### Task 2

pyspark --packages com.databricks:spark-csv_2.10:1.5.0

irisrdd = sc.textFile('/user/kaushik/iris.csv').map(lambda l: l.split(',')).map(lambda l: (float(l[0]),float(l[1]),float(l[2]),float(l[3]),str(l[4])))

from pyspark.sql.types import *
schema = StructType([StructField("sep_len", FloatType(), True),
    StructField("sep_wid",FloatType(),True),
    StructField("pet_len",FloatType(),True),
    StructField("pet_wid",FloatType(), True),
    StructField("species", StringType(),True)
])
irisdf = sqlContext.createDataFrame(irisrdd,schema)
irisdf.show()
+-------+-------+-------+-------+-----------+
|sep_len|sep_wid|pet_len|pet_wid|    species|
+-------+-------+-------+-------+-----------+
|    5.1|    3.5|    1.4|    0.2|Iris-setosa|
|    4.9|    3.0|    1.4|    0.2|Iris-setosa|
|    4.7|    3.2|    1.3|    0.2|Iris-setosa|
|    4.6|    3.1|    1.5|    0.2|Iris-setosa|
|    5.0|    3.6|    1.4|    0.2|Iris-setosa|
|    5.4|    3.9|    1.7|    0.4|Iris-setosa|
|    4.6|    3.4|    1.4|    0.3|Iris-setosa|
|    5.0|    3.4|    1.5|    0.2|Iris-setosa|
|    4.4|    2.9|    1.4|    0.2|Iris-setosa|
|    4.9|    3.1|    1.5|    0.1|Iris-setosa|
|    5.4|    3.7|    1.5|    0.2|Iris-setosa|
|    4.8|    3.4|    1.6|    0.2|Iris-setosa|
|    4.8|    3.0|    1.4|    0.1|Iris-setosa|
|    4.3|    3.0|    1.1|    0.1|Iris-setosa|
|    5.8|    4.0|    1.2|    0.2|Iris-setosa|
|    5.7|    4.4|    1.5|    0.4|Iris-setosa|
|    5.4|    3.9|    1.3|    0.4|Iris-setosa|
|    5.1|    3.5|    1.4|    0.3|Iris-setosa|
|    5.7|    3.8|    1.7|    0.3|Iris-setosa|
|    5.1|    3.8|    1.5|    0.3|Iris-setosa|
+-------+-------+-------+-------+-----------+
only showing top 20 rows
irisdf.registerTempTable('iris')
sqlContext.sql('select * from iris limit 2')
DataFrame[sep_len: float, sep_wid: float, pet_len: float, pet_wid: float, species: string]
sqlContext.sql('select * from iris limit 2').show()
+-------+-------+-------+-------+-----------+
|sep_len|sep_wid|pet_len|pet_wid|    species|
+-------+-------+-------+-------+-----------+
|    5.1|    3.5|    1.4|    0.2|Iris-setosa|
|    4.9|    3.0|    1.4|    0.2|Iris-setosa|
+-------+-------+-------+-------+-----------+

query = sqlContext.sql('select * from original_iris where s_length < 5 limit 20')
query
DataFrame[s_length: int, s_width: int, p_length: int, p_width: int, species: string]
query.write.format('com.databricks.spark.csv').save('/user/kaushik/querycsv')

hdfs dfs -cat /user/kaushik/querycsv/part-00000

### setconfig avro

sqlContext.setConf("spark.sql.parquet.compression.codec.", "codec")
sqlContext.setConf("spark.sql.avro.compression.codec","codec")


### task 3

#### Compression

## PARQUET

sqlContext.setConf("spark.sql.parquet.compression.codec","snappy")

votedf.write.mode("overwrite").format("parquet").save('/user/kaushik/finalparquet')

sqlContext.setConf("spark.sql.parquet.compression.codec","gzip")

votedf.write.mode("overwrite").format("parquet").save('/user/kaushik/finalparquetgzip')

sqlContext.setConf("spark.sql.parquet.compression.codec","uncompressed")

votedf.write.mode("overwrite").format("parquet").save('/user/kaushik/finalparquetuncompressed')

## AVRO

##### Default compresssion is snappy

sqlContext.setConf("spark.sql.avro.compression.codec","deflate")
sqlContext.setConf("spark.sql.avro.deflate.level", "5")
df.write.format('com.databricks.spark.avro').save('/user/kaushik/databricksavrodeflate')
sqlContext.setConf("spark.sql.avro.compression.codec","uncompressed")
df.write.format('com.databricks.spark.avro').save('/user/kaushik/databricksuncompressed')

### task 4 

violation = sqlContext.read.format("com.databricks.spark.csv").option('header','true').load("/user/kaushik/violations_plus.csv")

violation.registerTempTable('violation')

sqlContext.sql('select risk_category,count(*) as count from violation group by risk_category order by count desc').show()

group = sqlContext.sql('select risk_category,count(*) as count from violation group by risk_category order by count
 desc')

group.write.format("com.databricks.spark.csv").option('header','true').save("/user/kaushik/group1")


### task 5 

depts = sqlContext.read.json('/user/kaushik/depts.json')

#### get schema

depts.printSchema()

depts.show(2)

depts.columns

depts.describe().show()

depts.describe('department_id').show()

depts.select('department_id','department_name').show(5)

depts.select('department_name').distinct().show()


### task 6 

create database pyspark;
use pyspark;
create table pyspark.customer (id int, first_name string,last_name string)
comment 'customer details'
row format delimited
fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/kaushik/hive_database';

df.write.format('com.databricks.spark.csv').option('header','true').option('codec','org.apache.hadoop.io.compress.GzipCodec').save('/user/kaushik/irisiris')

save.write.format('orc').option('header','true').save('/user/kaushik/iriskaushiks')


df = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').load('/user/kaushik/iris.csv')

rdd1 = sqlContext.read.format('com.databricks.spark.csv').option('delimiter','\t').option('inferschema','true').load('/user/kaushik/Vote.txt')

rdd1.toDF('u','p','l','h','y')

uj.select('u').distinct().count()

### Take two tsv files, join them and save it to hdfs 

item = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Items.tsv')

order.printSchema()

order.filter(order.Quantity<100).show()

### Convert string to date

orders = sqlContext.read.format('com.databricks.spark.csv').option('inferschema','true').option('delimiter','\t').load('/user/lkaushik_amaravadi/Lokad_Items.tsv')

schema = Structtype([StructField('Id',Integertype(),True),StructField('Date',DateType(),True),StructField('Quantity',IntegerType(),True)])



from pyspark.sql.functions import *

func = udf(lambda x: datetime.strptime(x, '%Y/%d/%m'),DateType())

 df = o.withColumn('Date',func(col('Date')))

### top n rows in each id 

from pyspark.sql.window import Window

window = Window.partitionBy(order['Id']).orderBy(order['Quantity'].desc())

from pyspark.sql.functions import rank, col

order.select('*', rank().over(window).alias('rank')).filter(col('rank') <= 2).show()


