# Apache Spark

Apache Spark is a lightning-fast cluster computing technology, designed for fast computation.  The main feature of Spark is its in-memory cluster computing
that increases the processing speed of an application. 

Spark is one of Hadoop’s sub project developed in 2009 in UC Berkeley’s AMPLab by
Matei Zaharia. It was Open Sourced in 2010 under a BSD license. It was donated to
Apache software foundation in 2013, and now Apache Spark has become a top level
Apache project from Feb-2014

Standalone
Hadoop Yarn
Spark in Mapreduce

## Apache Spark Core
Spark Core is the underlying general execution engine for spark platform that all other
functionality is built upon. It provides In-Memory computing and referencing datasets in
external storage systems.

Spark SQL - Module for working with structured data. Allows you to seamlessly mix SQL queries with Spark programs.
Spark Streaming - API that allows you to build scalable fault-tolerant streaming applications.
MLlib - API that implements common machine learning algorithms.
GraphX - API for graphs and graph-parallel computation.

### RDD 

Resilient Distributed Datasets (RDD) is a fundamental data structure of Spark. It is an
immutable distributed collection of objects. Each dataset in RDD is divided into logical
partitions, which may be computed on different nodes of the cluster. RDDs can contain
any type of Python, Java, or Scala objects, including user-defined classes.
Formally, an RDD is a read-only, partitioned collection of records. RDDs can be created
through deterministic operations on either data on stable storage or other RDDs. RDD is
a fault-tolerant collection of elements that can be operated on in parallel.
There are two ways to create RDDs: parallelizing an existing collection in your driver
program, or referencing a dataset in an external storage system, such as a shared file
system, HDFS, HBase, or any data source offering a Hadoop Input Format.
Spark makes use of the concept of RDD to achieve faster and efficient MapReduce
operations.

The key idea of spark is Resilient Distributed Datasets (RDD); it supports inmemory
processing computation. This means, it stores the state of memory as an object
across the jobs and the object is sharable between those jobs. Data sharing in memory
is 10 to 100 times faster than network and Disk



RDD transformations returns pointer to new RDD and allows you to create dependencies
between RDDs. Each RDD in dependency chain (String of Dependencies) has a function
for calculating its data and has a pointer (dependency) to its parent RDD
Spark is lazy, so nothing will be executed unless you call some transformation or action
that will trigger job creation and execution. 

### TRANFORMATION

map(func)
Returns a new distributed dataset, formed by passing each element of the
source through a function func


filter(func)
Returns a new dataset formed by selecting those elements of the source on
which func returns true

flatMap(func)
Similar to map, but each input item can be mapped to 0 or more output
items (so func should return a Seq rather than a single item).


RDD
....
RDD is big collection of data

Resilient-fault tolerant

Distributed-can run on multiple machines

Data set-collection of data



properties
..........

immutable:once created never changes(Helps in parallelize and caching)

lazy evaluated:do not compute transformations till u need it or until an action is made
                until then loaded RDD are empty in memory
example :
val c1=collection.map(value=>value+1)
val c2=c1.map(value=>value+2)
print c2(now transform)(val c2=collection.map(value=>{var result=value+1 result=result+2}}

cachable(immutable data can be cached)


type inference(no type casting of data is required)(data type is not required)

sequence of steps performed on RDD
..................................
Transformations(map or join) 

actions(print)

Dependencies of RDD
.....................

Narrow(each partition of the parent RDD is used by at most one partition of the child RDD)

Wide(multiple child RDD partitions may depend on a single parent RDD partition)



Introduction about spark
........................
spark is built on scala about 1500 lines of code 

which is faster in execution

we can use intermediate results

we do in memory computation
 
spark modes of execution
......................
local mode(lacks proper troubleshooting)
yarn (for production)
mesos(for production)
standlone(development and troubleshoot in cluster mode)


spark modules
.................
core spark(transformations:map,join and actions:reduce,count,collect)

Dataframes,datasets and sql(integration of rdd with sql by ceating structure at run time)

Spark streaming(for analytics for batch data from  sources such as web sources using flu and kafka) 

Mlib(to apply machine learning algorithms)

Graphx(for graph pocessing )

Bagel(for implemeting graph processing algorithms)

R(for working with R like spark with scala)


Engine
........
Spark Core

storage
.........
local 
hdfs
rdbms
nosql

supported programming interfaces
.................................
scala
python
r
java
tools



Spark job anatomy
....................

Driver program(in master machine)
workernode(data node)
executors(code is sitting....space in ram where block is loaded where you can cache to persist data)





