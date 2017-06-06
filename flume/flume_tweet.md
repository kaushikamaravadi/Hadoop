TwitterAgent.sources = Twitter 
TwitterAgent.channels = MemChannel 
TwitterAgent.sinks = HDFS
  
# Describing/Configuring the source 
TwitterAgent.sources.Twitter.type = org.apache.flume.source.twitter.TwitterSource
TwitterAgent.sources.Twitter.consumerKey=F8EQO6fBSNpIFLE3FL2kMXU2s
TwitterAgent.sources.Twitter.consumerSecret=vwP6fojKEeQtnKhEHImwqJVpVZ55OpR3naR4LjOiy06Waf5WWv
TwitterAgent.sources.Twitter.accessToken=839904654968356868-vGhnDlTffwBa5UUjHTql8p3r8HqjvJG
TwitterAgent.sources.Twitter.accessTokenSecret=i6D9gasWncIyOCJNyo79njoPWiceAC20DZ40Axi3N54Ni
TwitterAgent.sources.Twitter.keywords=python,numpy,pandas,zeppelin,git,hadoop,spark
# Describing/Configuring the sink 

TwitterAgent.sources.Twitter.keywords= python,numpy,pandas,zeppelin,git,hadoop,spark

TwitterAgent.sinks.HDFS.channel=MemChannel
TwitterAgent.sinks.HDFS.type=hdfs
TwitterAgent.sinks.HDFS.hdfs.path=hdfs://130.211.217.244:9000/user/flume/tweets
TwitterAgent.sinks.HDFS.hdfs.fileType=DataStream
TwitterAgent.sinks.HDFS.hdfs.writeformat=Text
TwitterAgent.sinks.HDFS.hdfs.batchSize=1000
TwitterAgent.sinks.HDFS.hdfs.rollSize=0
TwitterAgent.sinks.HDFS.hdfs.rollCount=10000
TwitterAgent.sinks.HDFS.hdfs.rollInterval=600

TwitterAgent.channels.MemChannel.type=memory
TwitterAgent.channels.MemChannel.capacity=10000
TwitterAgent.channels.MemChannel.transactionCapacity=1000

TwitterAgent.sources.Twitter.channels = MemChannel
TwitterAgent.sinks.HDFS.channel = MemChannel
