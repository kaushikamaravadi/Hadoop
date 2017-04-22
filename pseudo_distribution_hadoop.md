### Update the source list

'''sh
sudo apt-get update
```

### Installing JAVA

'''sh
sudo apt-get install default-jdk
```

```sh
java -version
```
```sh
update-alternatives --config java
```

### Installing SSH

```sh
sudo apt-get install ssh
```
```sh
which ssh
```
```sh
ssh-keygen
```
```sh
cat ./.ssh/id_rsa.pub > ./.ssh/authorized_keys
```
```sh
ssh localhost
```


### Installing Hadoop

Download Hadoop from the Apache Download Mirrors and extract the contents of the Hadoop package to a location of your choice.

## http://mirror.jax.hugeserver.com/apache/hadoop/core/

```sh
tar xvzf hadoop-3.0.0-alpha2.tar.gz 
```

These are the following files we need to edit

~/.bashrc
/usr/local/hadoop/etc/hadoop/hadoop-env.sh
/usr/local/hadoop/etc/hadoop/core-site.xml
/usr/local/hadoop/etc/hadoop/mapred-site.xml.template
/usr/local/hadoop/etc/hadoop/hdfs-site.xml

```sh
vi ~/.bashrc
```
## Append to the end of ~/.bashrc

```sh
#HADOOP VARIABLES START
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_INSTALL=/home/ubuntu/hadoop_3
export PATH=$PATH:$HADOOP_INSTALL/bin
export PATH=$PATH:$HADOOP_INSTALL/sbin
export HADOOP_MAPRED_HOME=$HADOOP_INSTALL
export HADOOP_COMMON_HOME=$HADOOP_INSTALL
export HADOOP_HDFS_HOME=$HADOOP_INSTALL
export YARN_HOME=$HADOOP_INSTALL
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_INSTALL/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_INSTALL/lib"
#HADOOP VARIABLES END
```
```sh
source ~/.bashrc
```

### We need to set java in hadoop-env.sh

```sh
vi hadoop_3/etc/hadoop/hadoop-env.sh
```
```sh
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

### we need to add content in core-site.xml

```sh
sudo mkdir -p /app/hadoop/tmp
```
```sh
sudo chmod 777 /app/hadoop/tmp
```

```sh
<configuration>
 <property>
  <name>hadoop.tmp.dir</name>
  <value>/app/hadoop/tmp</value>
  <description>A base for other temporary directories.</description>
 </property>

 <property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:54310</value>
  <description>The name of the default file system.  A URI whose
  scheme and authority determine the FileSystem implementation.  The
  uri's scheme determines the config property (fs.SCHEME.impl) naming
  the FileSystem implementation class.  The uri's authority is used to
  determine the host, port, etc. for a filesystem.</description>
 </property>
</configuration>
```

### We need to add the below in mapred-site.xml

```sh
mv etc/hadoop/mapred-site.xml.template etc/hadoop/mapred-site.xml
```

```sh
<configuration>
<property>
  <name>mapred.job.tracker</name>
  <value>localhost:54311</value>
  <description>The host and port that the MapReduce job tracker runs
  at.  If "local", then jobs are run in-process as a single map
  and reduce task.
  </description>
 </property>
</configuration>
```

### We need to add this in hdfs-site.xml

```sh
mkdir -p /home/ubuntu/hadoop_3/datanode
mkdir -p /home/ubuntu/hadoop_3namenode
vi etc/hadoop/hdfs-site.xml
```
```sh
<configuration>
<property>
  <name>dfs.replication</name>
  <value>1</value>
  <description>Default block replication.
  The actual number of replications can be specified when the file is created.
  The default is used if replication is not specified in create time.
  </description>
 </property>
 <property>
   <name>dfs.namenode.name.dir</name>
   <value>file:/home/ubuntu/hadoop_3/namenode</value>
 </property>
 <property>
   <name>dfs.datanode.data.dir</name>
   <value>file:/home/ubuntu/hadoop_3/datanode</value>
 </property>
</configuration>
```





