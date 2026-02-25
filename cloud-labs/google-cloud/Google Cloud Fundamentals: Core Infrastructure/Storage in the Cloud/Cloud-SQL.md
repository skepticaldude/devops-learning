Google Cloud’s second core storage option is Cloud SQL.

Cloud SQL offers fully managed relational databases, including MySQL, PostgreSQL, and SQL Server as a service.

It’s designed to hand off mundane, but necessary and often time-consuming, tasks to Google—like applying

patches and updates managing backups, and configuring replications—so your focus can be on building great applications.

Cloud SQL doesn't require any software installation or maintenance.

It can scale up to 128 processor cores, 864 GB of RAM, and 64 TB of storage.

It supports automatic replication scenarios, such as from a Cloud SQL primary instance, an external primary instance, and external MySQL instances.

Cloud SQL supports managed backups, so backed-up data is securely stored and accessible if a restore is required.

The cost of an instance covers seven backups.

Cloud SQL encrypts customer data when on Google’s internal networks and when stored in database tables, temporary files, and backups.

And it includes a network firewall, which controls network access to each database instance.

A benefit of Cloud SQL instances is that they are accessible by other Google Cloud services, and even external services.

Cloud SQL can be used with App Engine using standard drivers like Connector/J for Java or MySQLdb for Python.

Compute Engine instances can be authorized to access Cloud SQL instances and configure the Cloud SQL instance to be in the same zone as your virtual machine.

Cloud SQL also supports other applications and tools that you might use, like SQL Workbench, Toad, and other external applications using standard MySQL drivers.
