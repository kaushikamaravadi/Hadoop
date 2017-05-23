# SqlContext

>>> sqlContext
<pyspark.sql.context.HiveContext object at 0x1850210>
>>> sqlContext = SQLContext(sc)
>>> deptsjson = sqlContext.jsonFile('/user/kaushik/depts.json')
/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/spark/python/pyspark/sql/context.py:478: UserWarning: jsonFi
le is deprecated. Use read.json() instead.
  warnings.warn("jsonFile is deprecated. Use read.json() instead.")

djson = sqlContext.read.json('/user/kaushik/depts.json')

>>> djson = sqlContext.read.json('/user/kaushik/depts.json')
>>> djson.registerTempTable('deptsTable')
>>> deptsdata = sqlContext.sql('select * from deptsTable')
>>> deptsdata.take(5)
[Row(department_id=2, department_name=u'Fitness'), Row(department_id=3, department_name=u'Footwear'), Row(departmen
t_id=4, department_name=u'Apparel'), Row(department_id=5, department_name=u'Golf'), Row(department_id=6, department
_name=u'Outdoors')]

deptsdata.write.json('/user/kaushik/cca/deptsjson')
