# HiBench

## The BigData Micro Benchmark suite

## OVERVIEW
HiBench is a big data benchmark suite that helps evaluate different big data frameworks in terms of speed, throughput and system resource utilizations. It contains a set of Hadoop, Spark and streaming workloads, including Sort, WordCount, TeraSort, Sleep, SQL, PageRank, Nutch indexing, Bayes, Kmeans, NWeight and enhanced DFSIO, etc. It also contains several streaming workloads for Spark Streaming, Flink, Storm and Gearpump.

## Build Hibench

To Build Hibench we need to clone the HiBench

### Git Clone

```sh
git clonehttps://github.com/intel-hadoop/HiBench.git
```

### Build All

To simply build all modules in Hibench, use the below command. This could be time consuming because the hadoopbench relies on 3rd party tools like Mahout and Nutch. The build process automatically downloads these tools for you. If you won't run these workloads, you can only build a specific framework to speed up the build process.

```sh
mvn -Dscala=2.11 clean package
```

### Build a specific framework benchmark

HiBench 6.0 supports building only bechmarks for a specific framework. For example, to build the hadoop benchmarks only, we can use the below command

```sh
mvn -Phadoopbench -Dscala=2.11 clean package 
```

To build hadoop and spark benchmarks

```sh
mvn -Phadoopbench -Psparkbench -Dscala=2.11 clean package
```
### Specify Scala Version

To specify the Scala version, use -Dscala=xxx(2.10 or 2.11). By default, it builds for scala 2.11.

```sh
mvn -Dscala=2.10 clean package
```


### Specify Spark Version

To specify the spark version, use -Dspark=xxx(1.6, 2.0 or 2.1). By default, it builds for spark 2.0

```sh
mvn -Psparkbench -Dspark=1.6 -Dscala=2.11 clean package
```

### Setup
 
 * Python 2.x(>=2.6) is required.
 
 * Supported Hadoop version: Apache Hadoop 2.x, CDH5.x, HDP 
 
 * Start HDFS, Yarn in the cluster.


### Configure `hadoop.conf`

Create and edit `conf/hadoop.conf`：
```sh
cp conf/hadoop.conf.template conf/hadoop.conf
```

####Set the below properties properly:

Property        |      Meaning
----------------|--------------------------------------------------------
hibench.hadoop.home     |      The Hadoop installation location
hibench.hadoop.executable  |   The path of hadoop executable. For Apache Hadoop, it is /YOUR/HADOOP/HOME/bin/hadoop
hibench.hadoop.configure.dir | Hadoop configuration directory. For Apache Hadoop, it is /YOUR/HADOOP/HOME/etc/hadoop
hibench.hdfs.master       |    The root HDFS path to store HiBench data, i.e. hdfs://localhost:8020/user/username
hibench.hadoop.release    |    Hadoop release provider. Supported value: apache, cdh5, hdp

```sh
hibench.hadoop.home             /opt/cloudera/parcels/CDH/lib/hadoop
hibench.hadoop.executable       /usr/bin/hadoop
hibench.hadoop.configure.dir    /etc/hadoop/conf
hibench.hdfs.master             /user/yeshwanth43/
hibench.hadoop.release          cdh5
hibench.slaves.hostnames        datanode2,namenode
hibench.master.hostnames        datanode1
```

### Micro Benchmarks

To run a `wordcount`

```sh
./bin/workloads/micro/wordcount/prepare/prepare.sh
```
```sh
./bin/workloads/micro/wordcount/hadoop/run.sh
```

To run a `sort`

```sh
./bin/workloads/micro/sort/prepare/prepare.sh
```
```sh
./bin/workloads/micro/sort/hadoop/run.sh
```
To run a `terasort`

```sh
./bin/workloads/micro/terasort/prepare/prepare.sh
```
```sh
./bin/workloads/micro/terasort/hadoop/run.sh
```
To run a `sleep`

```sh
./bin/workloads/micro/sleep/prepare/prepare.sh
```
```sh
./bin/workloads/micro/sleep/hadoop/run.sh
```
To run a `dfsioe`

```sh
./bin/workloads/micro/dfsioe/prepare/prepare.sh
```
```sh
./bin/workloads/micro/dfsioe/hadoop/run.sh
```

### Websearch Benchmarks

```sh
./HiBench/bin/workloads/websearch/nutchindexing/prepare/prepare.sh
```
```sh
./HiBench/bin/workloads/websearch/nutchindexing/hadoop/run.sh 
```

### SQL

To run a `sql`

```sh
./bin/workloads/sql/scan/prepare/prepare.sh
```
```sh
./bin/workloads/sql/scan/hadoop/run.sh
```

```sh
./bin/workloads/sql/join/prepare/prepare.sh
```
```sh
./bin/workloads/sql/join/hadoop/run.sh
```
```sh
./bin/workloads/sql/aggregation/prepare/prepare.sh
```
```sh
./bin/workloads/sql/aggregation/hadoop/run.sh
```

### View the report

The `<HiBench_Root>/report/hibench.report` is a summarized workload report, including workload name, execution duration, data size, throughput per cluster, throughput per node.

```sh
/HiBench/report
```

