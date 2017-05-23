# spark-submit

### saveAsSequenceFile

```python
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('pyspark')
sc = SparkContext(conf=conf)
data = sc.textFile('/user/kaushik/Vote.txt').flatMap(lambda x: x.split('\t'))
data.map(lambda x: (None,x)).saveAsSequenceFile('/user/kaushik/pysparkseq22')
```
```sh
spark-submit --master yarn saveassequencefile.py
```

```sh
hdfs dfs -ls /user/kaushik/pysparkseq22
```
Found 3 items
-rw-r--r--   1 root kaushik_santosh14          0 2017-05-19 21:30 /user/kaushik/pysparkseq22/_SUCCESS
-rw-r--r--   1 root kaushik_santosh14  109127192 2017-05-19 21:30 /user/kaushik/pysparkseq22/part-00000
-rw-r--r--   1 root kaushik_santosh14  108137000 2017-05-19 21:30 /user/kaushik/pysparkseq22/part-00001



### Wordcount

```python
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('pyspark')
sc = SparkContext(conf=conf)
# Reading data from HDFS location
# Flatten each line into multiple words using ” ” (space) as delimiter.
data = sc.textFile('/user/kaushik/pyspark/wordcount/wordcount.txt').flatMap(lambda x: x.split(' '))
# Associate value 1 for each of the input word to map function.
datamap = data.map(lambda x: (x,1))
# Aggregating using key (which are nothing but all unique words)
datareducebykey = datamap.reduceByKey(lambda x,y: x+y)
# Saving to HDFS
datareducebykey.saveAsTextFile('/user/kaushik/pyspark/wordcount/wordcountoutput')

### Validation

```sh
hdfs dfs -ls /user/kaushik/pyspark/wordcount/wordcountoutput
```
```
Found 3 items
-rw-r--r--   1 root kaushik_santosh14          0 2017-05-19 22:08 /user/kaushik/pyspark/wordcount/wordcountoutput/_SUCCESS
-rw-r--r--   1 root kaushik_santosh14        523 2017-05-19 22:08 /user/kaushik/pyspark/wordcount/wordcountoutput/part-00000
-rw-r--r--   1 root kaushik_santosh14        580 2017-05-19 22:08 /user/kaushik/pyspark/wordcount/wordcountoutput/part-00001
```
