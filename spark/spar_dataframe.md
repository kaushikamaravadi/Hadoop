iris = sc.textFile('/user/kaushik_santosh14/iris.csv').map(lambda x: x.split(','))
>>> irisdata = iris.toDF()
>>> irisdata
DataFrame[_1: string, _2: string, _3: string, _4: string, _5: string]
