## Hive

Hive is a data warehouse software which is used for facilitates querying and managing large data sets residing in distributed storage.Hive language almost look like SQL language called HiveQL.Hive is designed to enable easy data summarization.Hive also allows traditional map reduce programs to customize mappers and reducers when it is inconvenient or inefficient to execute the logic in HiveQL (User Defined Functions UDFS).

Hive is not designed for online transaction supports and does not offer real-time queries and row level updates. It is best used for batch jobs over large sets of immutable data (like web logs)

The Stinger Initiative successfully delivered a fundamental new Apache Hive, which evolved Hive’s traditional architecture and made it faster, with richer SQL semantics and petabyte scalability.


### Hive Features Included

Easy to enable tools for ETL(extract/transform/load)

Stores variety of data

Directly store the data on top of HDFS or Apache Hbase

Mapreduce Execution Internally

Best used for batch jobs over large sets of append-only data (like web logs).

Users very comfortable with SQL

Developed by facebook and contributed by facebook

Custom, aggregations,table functions available UDFs (User defined functions) UDAFs(User defined aggregation functions),and table functions (UDTF’s).

Hive works equally well on Thrift

Apache Derby default one for Hive ,Mysql can optionally be used

Currently, there are four file formats supported in Hive, which are TEXTFILE, SEQUENCEFILE, ORC and RCFILE.

Hctalog is used when Hbase or others want to access the hive metastore


### Hive Applications Include

Data Mining
Document Indexing
Predictive modeling, and Hypothesis testing
Customer-facing Business Intelligence (e.g., Google Analytics)
Log processing
Hive is not designed for OLTP workloads and does not offer real-time queries or row-level updates.

### Major Components of Hive 

UI :- UI means User Interface, The user interface for users to submit queries and other operations to the system.

Driver :- The Driver is used for receives the quires from UI .This component implements the notion of session handles and provides execute and fetch APIs modeled on JDBC/ODBC interfaces.

Compiler :- The component that parses the query, does semantic analysis on the different query blocks and query expressions and eventually generates an execution plan with the help of the table and partition metadata looked up from the metastore.

MetaStore :-  The component that stores all the structure information of the various tables and partitions in the warehouse including column and column type information, the serializers and deserializers necessary to read and write data and the corresponding HDFS files where the data is stored.

Execution Engine :- The component which executes the execution plan created by the compiler. The plan is a DAG of stages. The execution engine manages the dependencies between these different stages of the plan and executes these stages on the appropriate system components.
