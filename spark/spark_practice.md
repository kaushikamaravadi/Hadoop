## Spark can directly create RDDs from text files

```
data = sc.textFile('/user/kaushik_santosh14/iris.csv')
data.take(5)
data.count()
```

# 'parallelize' creates an RDD by distributing data over the cluster

```
rdd = sc.parallelize(range(14), numSlices=4)
print("Number of partitions: {}".format(rdd.getNumPartitions()))
```

# 'glom' lists all elements within each partition

```
print(rdd.glom().collect())
rddSquared = rdd.map(lambda x: x ** 2)
```

# def squared(x):
#     return x ** 2
# rddSquared = rdd.map(squared)

```
rddSquared.take(10)
```

# Popular transformations
# -----------------------

```
func = lambda x: -x
rdd.map(func)
rdd.flatMap(func) # like map, but flattens results
rdd.filter(func)
rdd.sortBy(func)
```

# Popular actions
# ---------------

```
rdd.reduce(lambda x, y: x + y)
rdd.count()
```

# Actions with which to take data from an RDD:

```

print(rdd.collect())                    # get all elements
print(rdd.first())                      # get first element
print(rdd.take(5))                      # get N first elements
print(rdd.top(3))                       # get N highest elements in descending order
print(rdd.takeOrdered(7, lambda x: -x)) # get N first elements in ascending (or a function's) order
```

## RDDs support simple statistical actions


```
print(rdd.stats())
print(rdd.count())
print(rdd.sum())
print(rdd.mean())
print(rdd.stdev(), rdd.sampleStdev())
print(rdd.variance(), rdd.sampleVariance())
print(rdd.min(), rdd.max())
print(rdd.histogram(5))

```
## RDDs support set transformations

```
rddB = sc.parallelize(range(0, 26, 2))
print(rdd.union(rddB).collect()) # or: rdd + rddB
print(rdd.union(rddB).distinct().collect())
print(rdd.intersection(rddB).collect())
print(rdd.subtract(rddB).collect())
print(rdd.cartesian(rddB).collect())

```
# A broadcast variable is copied to each machine only once, in an efficient manner.
# It is very suitable when each node uses the data in it, and especially so if the data is
# large and would otherwise be sent across the network multiple times.

```

broadcastVar = sc.broadcast({'CA': 'California', 'NL': 'Netherlands'})
print(broadcastVar.value)
```

# An accumulator is a shared variable that lives on the master, and to
# which each task can add values. (Basically, it's a simple reducer.)
```
accu = sc.accumulator(0)
```
# 'foreach' just applies a function to each RDD element without returning anything

```
rdd.foreach(lambda x: accu.add(x))
print(accu.value)
```



>>> vote = sc.textFile('/user/kaushik/Vote.txt').map(lambda x: x.split('\t'))
>>> vote.take(2)

>>> sc.parallelize([2,3,4]).flatMap(lambda x: [x,x,x]).collect()
[2, 2, 2, 3, 3, 3, 4, 4, 4]

sc.parallelize([2,3,4]).map(lambda x: [x,x,x]).collect()
[[2, 2, 2], [3, 3, 3], [4, 4, 4]]

## Difference between parallelize and broadcast


sc.parallelize(...) spread the data amongst all executors

sc.broadcast(...) copy the data in the jvm of each executor

## MAPPARTITIONS(FUNC, PRESERVESPARTITIONING=FALSE)

>>> one_through_9 = range(1,10)
>>> parallel = sc.parallelize(one_through_9, 3)
>>> def f(iterator): yield sum(iterator)
>>> parallel.mapPartitions(f).collect()
[6, 15, 24]
 
>>> parallel = sc.parallelize(one_through_9)
>>> parallel.mapPartitions(f).collect()
[1, 2, 3, 4, 5, 6, 7, 17]
>>> print sc.defaultParallelism
2


## MAPPARTITIONSWITHINDEX(FUNC)

>>> parallel = sc.parallelize(range(1,10),4)
>>> def show(index, iterator): yield 'index: '+str(index)+" values: "+ str(list(iterator))
>>> parallel.mapPartitionsWithIndex(show).collect()

>>> parallel = sc.parallelize(range(1,10),3)
>>> def show(index, iterator): yield 'index: '+str(index)+" values: "+ str(list(iterator))
>>> parallel.mapPartitionsWithIndex(show).collect()

## SAMPLE(WITHREPLACEMENT,FRACTION, SEED)

>>> parallel = sc.parallelize(range(1,10))
>>> parallel.sample(True,.2).count()
3

withReplacement – can elements be sampled multiple times (replaced when sampled out)
fraction – expected size of the sample as a fraction of this RDD’s size without replacement: probability that each element is chosen; fraction must be [0, 1] with replacement: expected number of times each element is chosen; fraction must be >= 0
seed – seed for the random number generator

## UNION

>>> one = sc.parallelize(range(1,10))
>>> two = sc.parallelize(range(10,21))
>>> one.union(two).collect()
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


## THE KEYS
The group of transformation functions (groupByKey, reduceByKey, aggregateByKey, sortByKey, join) all act on key,value pair RDDs.


## JOIN(OTHERDATASET, [NUMTASKS])

>>> names1 = sc.parallelize(("abe", "abby", "apple")).map(lambda a: (a, 1))
>>> names2 = sc.parallelize(("apple", "beatty", "beatrice")).map(lambda a: (a, 1))
>>> names1.join(names2).collect()
[('apple', (1, 1))] 

>>> names1.union(names2).collect()
[('abe', 1), ('abby', 1), ('apple', 1), ('apple', 1), ('beatty', 1), ('beatrice', 1)]

>>> names1.intersection(names2).collect()
[('apple', 1)]
>>> names1.leftOuterJoin(names2).collect()
[('abe', (1, None)), ('apple', (1, 1)), ('abby', (1, None))]
>>> names1.rightOuterJoin(names2).collect()
[('apple', (1, 1)), ('beatrice', (None, 1)), ('beatty', (None, 1))]



# Vote

>>> vote = sc.textFile('/user/kaushik/Vote.txt').map(lambda x: x.split('\t'))
>>> vote.count()
2811983


>>> vote.map(lambda line: line[1]).distinct().count()
1623

vote.saveAsTextFile('/user/kaushik/pyspark_text')

sc.textFile("test.txt")\
  .map(lambda line: (line.split(',')[0], line.split(',')[1]))\
  .distinct()\
  .count()

>>> vote1.take(5)
[u'0.60', u'0.60', u'0.40', u'0.00', u'0.80']
>>> u = vote1.take(5)
>>> sc.parallelize(u,2).countByValue().items()
[(u'0.60', 2), (u'0.00', 1), (u'0.80', 1), (u'0.40', 1)]
# KIRITI ANNA YESWANTH ANNA


# Transformations on textFile

### Convert all words in a rdd to lowercase and split the lines of a document using space.

>>> def func(lines): 
...     lines = lines.lower()
...     lines = lines.split()
...     return lines
... 
>>> use1 = use.map(func)

>>> use2 = use.flatMap(func)
>>> use2.take(2)
[u'all', u'of']

###  Next, I want to remove the words, which are not necessary to analyze this text. We call these words as “stop words”; Stop words do not add much value in a text. For example, “is”, “am”, “are” and “the” are few examples of stop words.

>>> stopwords = ['is','am','are','the','for','a','of']
>>> use3 = use2.filter(lambda x: x not in stopwords)
>>> use3.take(5)
[u'all', u'above', u'explains', u'why', u'it\u2019s']

## Transformation: groupBy

### After getting the results into rdd3, we want to group the words in rdd3 based on which letters they start with. For example, suppose I want to group each word of rdd3 based on first 3 characters.

>>> use4 = use3.groupBy(lambda w: w[0:3])
>>> print [(k, list(v)) for (k,v) in use4.take(1)]
[(u'all', [u'all'])]
>>> use3_mapped =use3.map(lambda x: (x,1))
>>> use3_grouped = use3_mapped.groupByKey()
>>> print(list((j[0], list(j[1])) for j in use3_grouped.take(5)))
[(u'all', [1]), (u'rdds.', [1]), (u'have', [1]), (u'type-safety', [1]), (u'when', [1, 1])]
>>> use3.filter(lambda x: x == 'all').collect()
[u'all']
>>> use3.filter(lambda x: x == 'when').collect()
[u'when', u'when']
>>> use3.filter(lambda x: x == 'rdds.').collect()
[u'rdds.']
>>> use3_freq_of_words = use3_grouped.mapValues(sum).map(lambda x: (x[1],x[0])).sortByKey(False)
>>> use3_freq_of_words.take(10)
[(4, u'you'), (4, u'to'), (4, u'that'), (3, u'use'), (3, u'in'), (2, u'when'), (2, u'want'), (2, u'api,'), (2, u'might')
, (2, u'python')]
>>> 



