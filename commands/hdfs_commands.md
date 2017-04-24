# Hadoop Commands

## classpath

Prints the class path needed to get the Hadoop jar and the required libraries
--glob	expand wildcards
--jar path	write classpath as manifest in jar named path
- h, --help	print help
```
hadoop classpath
```
/etc/hadoop/conf:/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/hadoop/libexec/../../hadoop/lib/*:/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/hadoop/libexec/../../hadoop/.//*:/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/hadoop/libexec/../../hadoop-hdfs/./:/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/hadoop/libexec/../../hadoop-hdfs/lib/*:/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/hadoop/libexec/../../hadoop-hdfs/.//*:/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/hadoop/libexec/../../hadoop-yarn/lib/*:/opt/cloudera/parcels/CDH-5.10.1-1.cdh5.10.1.p0.10/lib/hadoop/libexec/../../hadoop-yarn/.//*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/lib/*:/opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/.//*

## hdfs dfs 

Run a filesystem command on the file system supported in Hadoop. The various COMMAND_OPTIONS can be found at File System Shell Guide.
Usage: hdfs dfs [Generic option]
```sh
- conf <configuration file>     specify an application configuration file
- D <property=value>            use value for given property
- fs <local|namenode:port>      specify a namenode
- jt <local|resourcemanager:port>    specify a ResourceManager
- files <comma separated list of files>    specify comma separated files to be copied to the map reduce cluster
- libjars <comma separated list of jars>    specify comma separated jar files to include in the classpath.
- archives <comma separated list of archives>    specify comma separated archives to be unarchived on the compute ma
chines.
```

## fetchdt

## fsck

path	Start checking from this path.
* -delete	Delete corrupted files.
* -files	Print out files being checked.
* -files -blocks	Print out the block report
* -files -blocks -locations	Print out locations for every block.
* -files -blocks -racks	Print out network topology for data-node locations.
* -files -blocks -replicaDetails	Print out each replica details.
* -files -blocks -upgradedomains	Print out upgrade domains for every block.
* -includeSnapshots	Include snapshot data if the given path indicates a snapshottable directory or there are snapshottable directories under it.
* -list-corruptfileblocks	Print out list of missing blocks and files they belong to.
* -move	Move corrupted files to /lost+found.
* -openforwrite	Print out files opened for write.
* -showprogress	Print out dots for progress in output. Default is OFF (no progress).
* -storagepolicies	Print out storage policy summary for the blocks.
* -maintenance	Print out maintenance state node details.
* -blockId	Print out information about the block.

```sh
hdfs fsck /user -blocks
```

```sh
Status: HEALTHY
 Total size:    530792249 B
 Total dirs:    551
 Total files:   662
 Total symlinks:                0
 Total blocks (validated):      659 (avg. block size 805451 B)
 Minimally replicated blocks:   659 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       658 (99.84825 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              1316 (66.63291 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Mon Apr 10 22:01:04 UTC 2017 in 259 milliseconds
The filesystem under path '/user' is HEALTHY
```

## getconf

- namenodes	gets list of namenodes in the cluster.
- secondaryNameNodes	gets list of secondary namenodes in the cluster.
- backupNodes	gets list of backup nodes in the cluster.
- includeFile	gets the include file path that defines the datanodes that can join the cluster.
- excludeFile	gets the exclude file path that defines the datanodes that need to decommissioned.
- nnRpcAddresses	gets the namenode rpc addresses
- confKey	gets a specific key from the configuration
```

```sh
hdfs getconf -namenodes
```

```sh
datanode.c.spatial-rookery-140916.internal
```

```sh
hdfs getconf -nnRpcAddresses
```
```sh
datanode.c.spatial-rookery-140916.internal:8022
```

## envvars

```sh
hdfs envvars
```

* display computed Hadoop environment variables.

## groups

Returns the group information given one or more usernames

```
hdfs groups
```

```sh
hdfs : hdfs hadoop
```

## secondarynamenode

-checkpoint [force]	Checkpoints the SecondaryNameNode if EditLog size >= fs.checkpoint.size. If force is used, checkpoint irrespective of EditLog size

-format	Format the local storage during startup.

-geteditsize	Prints the number of uncheckpointed transactions on the NameNode.

```sh
hdfs secondarynamenode -checkpoint 
```

## hdfs namenode

- backup	Start backup node.

- checkpoint	Start checkpoint node.

- format [-clusterid cid] [-force] [-nonInteractive]	Formats the specified NameNode. It starts the NameNode, formats it and then shut it down. -force option formats if the name directory exists. -nonInteractive option aborts if the name directory exists, unless -force option is specified.

- upgrade [-clusterid cid] [-renameReserved <k-v pairs>]	Namenode should be started with upgrade option after the distribution of new Hadoop version.

- upgradeOnly [-clusterid cid] [-renameReserved <k-v pairs>]	Upgrade the specified NameNode and then shutdown it.

- rollback	Rollback the NameNode to the previous version. This should be used after stopping the cluster and distributing the old Hadoop version.

- rollingUpgrade <rollback|started>	See Rolling Upgrade document for the detail.

- importCheckpoint	Loads image from a checkpoint directory and save it into the current one. Checkpoint dir is read from property dfs.namenode.checkpoint.dir

- initializeSharedEdits	Format a new shared edits dir and copy in enough edit log segments so that the standby NameNode can start up.

- bootstrapStandby [-force] [-nonInteractive] [-skipSharedEditsCheck]	Allows the standby NameNode’s storage directories to be bootstrapped by copying the latest namespace snapshot from the active NameNode. This is used when first configuring an HA cluster. The option -force or -nonInteractive has the same meaning as that described in namenode -format command. -skipSharedEditsCheck option skips edits check which ensures that we have enough edits already in the shared directory to start up from the last checkpoint on the active.

- recover [-force]	Recover lost metadata on a corrupt filesystem. See HDFS User Guide for the detail.

- metadataVersion	Verify that configured directories exist, then print the metadata versions of the software and the image.
