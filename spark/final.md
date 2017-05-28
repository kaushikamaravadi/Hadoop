order_items = sqlContext.read.format('com.databricks.spark.csv').option('inferschema','true').load('/user/kaushik_amaravadi/order_items.csv')

orders = sqlContext.read.format('com.databricks.spark.csv').option('inferschema','true').load('/user/kaushik_amaravadi/orders.csv')




order = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').option('delimiter','\t').load('/user/kaushik/Lokad_Orders.tsv')

### on the filtered data set find out the higest value in the product_price column under each category

order.groupBy('Id').agg({'Quantity':'max'}).show()

### on the filtered data set also find out total products under each category

order.groupBy('Id').agg({'Quantity':'count'}).show()

### on the filtered data set also find out the average price of the product under each category

order.groupBy('Id').agg({'Quantity':'avg'}).show()

### on the filtered data set also find out the minimum price of the product under each category

order.groupBy('Id').agg({'Quantity':'min'}).show()


### sort by id ascending order

order.groupBy('Id').agg({'Quantity':'min'}).orderBy(order['Id'].asc()).show()

### sort by quantity descending order

select max(Quantity) as a, Id from order group by id order by a


sqlContext.setConf('spark.sql.avro.compression.codec','uncompressed')
order.write.format('com.databricks.spark.avro').save('/user/kaushik/avro')


sqlContext.setConf('spark.sql.parquet.compression.codec','snappy')


sqlContext.setConf('spar.sql.parquet.compression.codec','uncompressed')

org.apache.hadoop.io.compress.SnappyCodec

order.write.json('/
