titanic = sqlContext.read.format('com.databricks.spark.csv').option('header','true').option('inferschema','true').load('/user/kaushik/train.csv')

titanic.count()

titanic.crosstab('Sex','Survived').show()

titanic.select(titanic['Fare']).show()

titanic.groupby('Age').agg({'Fare':'mean'}).show()


### Order dataset

### Top N records from Order dataset
 
order.registerTempTable('order')
sqlContext.sql('select Quantity from order order by Quantity desc limit 10').show()

order.sort(order.Quantity.desc()).show()

order.sort('Quantity',ascending=False).show()

order.orderBy(order.Quantity.desc()).show()

order.orderBy(order.Quantity.asc()).show()

order.select(order['Id'],order['Quantity']).orderBy(order.Quantity.desc()).show()

order.groupby('Id').agg({'Quantity':'min'}).show()


### select min quantity in eacg id

sqlContext.sql('select id, min(quantity) as b from order group by id order by b').show()


### filter 

### All columns

order.filter(order['Quantity']>1900).show()

order.filter(order['Quantity'] == 1941).show()

### Only 'Id' and 'Quantity'

order.select(order['Id'],order['Quantity']).filter(order['Quantity']>1900).show()

### aggregation with group by

order.groupBy('Id').agg(F.max(order.Quantity)).show()

from pyspark.sql import functions as F

### max Quantity in each Id

order.groupBy('Id').max('Quantity').show()
order.groupby('Id').agg({'Quantity':'max'}).show()

### avg quantity

order.agg(F.avg(order.Quantity)).show()

order.groupBy('Id').agg(F.avg(order.Quantity)).show()

order.groupBy('Id').agg({'Quantity':'avg'}).show()

### 
