The last of Google Cloud’s core storage options we’re going to explore is Bigtable. 

Bigtable is Google's NoSQL big data database service.

It's the same database that powers many core Google services, including Search, Analytics, Maps, and Gmail.

Bigtable is designed to handle massive workloads at consistent low latency and high throughput, so it's a

great choice for both operational and analytical applications, including Internet of Things, user analytics, and financial data analysis.

When deciding which storage option is best, customers often choose Bigtable if: They’re working with more than 1TB of semi-structured or structured data.

Data is fast with high throughput, or it’s rapidly changing.

They’re working with NoSQL data.

This usually means transactions where strong relational semantics are not required.

Data is a time-series or has natural semantic ordering.

They’re working with big data, running asynchronous batch or synchronous real-time processing on the data.

Or they’re running machine learning algorithms on the data.

Bigtable can interact with other Google Cloud services and third-party clients.

Using APIs, data can be read from and written to Bigtable through a data service

layer like Managed VMs, the HBase REST Server, or a Java Server using the HBase client.

Typically this is used to serve data to applications, dashboards, and data services.

Data can also be streamed in through a variety of popular stream processing frameworks like; 
* Dataflow Streaming
* Spark Streaming
* and Storm.

And if streaming is not an option, data can also be read from and written to Bigtable through batch processes like
* Hadoop
* MapReduce
* Dataflow
* Spark.

Often, summarized or newly calculated data is written back to Bigtable or to a downstream database.
