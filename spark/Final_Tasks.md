## pyspark --packages com.databricks:spark-csv_2.11:1.5.0

## from pyspark.sql.types import *

### Sqoop Import

sqoop import --connect jdbc:mysql://localhost/pyspark --username root --password Srianjaneyam@34 --table titanic -m 1 --fields-terminated-by '\t' --target-dir "/user/kaushik_amaravadi/titanic"

### Sqoop Export



### Join two desperate datasets

```python
item = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Items.tsv')
```
```python
order = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Orders.tsv')
```
```python
df = item.join(order,['Id'])
```
```python
df.show()
```
```python
fianl = df.select(df['Id'],df['LabelName'],df['Quantity'])
```
```python
fianl.registerTempTable('final')
```
```python
thee = sqlContext.sql('select Quantity,concat(Id,LabelName) as Full from final')
```
```python

thee.show()
```

### 7 Columns

```python
item = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Items.tsv')
```
```python

sevencolumns=item.select(item['Id'],item['LabelName'],item['TagLabelCategory'],item['TagSubCategory'],item['ServiceLevel'],item['StockOnOrder'],item['StockOnHand'])

```

### Parquet gz Compression

```python
item = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Items.tsv')
```
```python
item.write.parquet('/user/kaushik/problem2')
```
### individual state count

```python
item = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Items.tsv')
```
```
item.registerTempTable('item')
```
```python
count = sqlContext.sql('select count(*) as count,LabelName from item group by LabelName order by count desc')
```
```python
count.write.format('com.databricks.spark.avro').save('/user/kaushik/problem3')
```

### query metastore Quantity > 100

sqlContext.sql('show databases').show()

sqlContext.sql('use ebay')

amount = sqlContext.sql('select * from final where Quantity>100 and Quantity<200 limit 10')

amount.show()

amount.write.format('com.databricks.spark.csv').save('/user/kaushik/quantity')

### Avro snappy

item = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Items.tsv')

item.write.format('com.databricks.spark.avro').save('/user/kaushik/problem7')

### Parquet Uncompressed

item = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/sparkjoin/Lokad_Items.tsv')

sqlContext.setConf("spark.sql.parquet.compression.codec","uncompressed")

item.write.mode("overwrite").format("parquet").save('/user/kaushik/problem8')


