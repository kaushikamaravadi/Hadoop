## Flume

If we want to load the data which is of type semi-structured and unstructured into the  HDFS cluster, or else capture the live streaming data which is generated, from different sources like twitter, weblogs and more into the HDFS cluster, which component of Hadoop ecosystem will be useful to do this kind of job. The solution is FLUME

### APACHE FLUME

Apache Flume is a Hadoop ecosystem component used to collect, aggregate and moves a large amount of log data from different sources to a centralized data store.

Flume Event: It is the main unit of the data that is transported inside the Flume (Typically a single log entry). It contains a payload of the byte array that is to be transported from the source path to the destination path which could be accompanied by optional headers

### COMPONENTS OF FLUME

#####Flume Agent

Is an independent Java virtual machine daemon process which receives the data (events) from clients and transports to the subsequent destination (sink or agent)

##### Source

Is the component of Flume agent which receives data from the data generators say, twitter, facebook, weblogs from different sites and transfers this data to one or more channels in the form of Flume event.The external source sends data to Flume in a format that is recognized by the target Flume source. Example, an Avro Flume source can be used to receive Avro data from Avro clients or other Flume agents in the flow that send data from an Avro sink, or the Thrift Flume source will receive data from a Thrift sink, or a Flume Thrift RPC client or Thrift Clients are written in any language generated from the Flume thrift protocol.

##### Channel

Once, the Flume source receives an Event, it stores this data into one or more channel and buffers them till they are consumed by sinks. It acts as a bridge between the source and sinks. These channels are implemented to handle any number of sources and sinks.

#####Sink
 
It stores the data into the centralized stores like HDFS and HBase.
