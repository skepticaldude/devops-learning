how to set up Cymbal Superstore’s cloud environment.

Let’s start with how to set up Cymbal Superstore’s cloud environment.
00:05
Cymbal Superstore is ready to start implementing basic cloud infrastructure for their organization.
00:10
As an Associate Cloud Engineer, you have been assigned to the team to help with this phase of the project.
00:16
The team begins with a planning meeting to decide how Cymbal Superstore’s cloud structure will be organized.
00:22
The outcomes of this phase of the migration journey include establishing a resource hierarchy, implementing organizational policies, managing projects and quotas, managing users and groups, and applying access management.
00:36
Setting up billing and monitoring the use of your cloud resources are also things to consider.
00:40
Let’s take a closer look.
00:43
How to set up a resource hierarchy on Google Cloud depends on the needs and structure of the organization.
00:49
Cymbal Superstore plans to migrate three applications to the cloud: its supply chain application, which will run on VMs; its containerized
00:57
ecommerce application, which will use GKE; and its transportation management application, which will use Cloud Run functions to track truck location.
01:07
These applications correspond to three different departments.
01:10
Operations manages the B2B supply chain, Logistics oversees transportation, and Sales & Marketing manages the eCommerce application.
01:20
The graphic shows a possible organizational hierarchy for Cymbal Superstore.
01:25
The Cymbal Superstore organization is at the top, followed by optional folders underneath, one for each division and one for each application.
01:32
There are multiple projects under the B2B supply chain app folder, one for each environment related to continuous integration/continuous delivery: a development, staging, and production environment.
01:43
Other apps in the chart would have a similar project structure.
01:47
As you set up the hierarchy, you will also need to grant organizational policies.
01:51
For example, Marketing might need to access the data in the supply chain system to see if inventory levels affected recent marketing campaigns.
02:00
Giving Marketing viewer permissions on the supply chain production environment might be a good choice to give them the access they need.
02:08
An Associate Cloud Engineer could also be tasked with enabling Application Programming Interfaces (API’s) within projects during setup.
02:16
Cymbal Superstore’s ecommerce project requires access to Google Kubernetes Engine and Cloud SQL as a database backend and you’ll need to enable the APIs for those services.
02:28
Setting up the cloud environment also involves granting members IAM roles to ensure that they have
02:32
the right access to projects depending on their needs of their job and role at Cymbal Superstore.
02:38
For example, data analysts in the Marketing department will need to have access to historic sales data in the ecommerce system.
02:46
This could be a great use case for BigQuery, Google Cloud’s data warehouse solution.
02:51
How would we go about giving proper access?
02:54
New data analysts would need to be added to the data_analyst group.
02:58
Managing permissions and rules at a group level is easier than keeping track of permissions for individual users.
03:04
Data analysts need to access the data in the dataset or table, so they require the bigquery.dataViewer role at the proper level.
03:13
Queries in BigQuery are executed as an executable job.
03:17
So to submit a query, a data analyst would also need the bigquery.jobs.create permission.
03:23
This permission is included in the predefined bigquery.user role.
03:28
You would give the data_analyst group access to this role in the Production project.
03:33
As a cloud engineer, you’ll need to know how to manage Cymbal Superstore’s users and groups in
03:37
Cloud Identity, a service for managing users and groups if you are not doing so via Google Workspace.
03:45
Google Cloud Observability, which used to be called Google Cloud’s operations suite and Stackdriver before that,
03:50
provides metrics and logging services for all of your services, resources, and projects in your cloud architecture.
03:57
To monitor metrics from multiple projects, you set up project scoping.
04:01
If Cymbal Superstore’s Operations department decides to monitor metrics across all three supply chain projects in the staging
04:06
environment project, you will set staging as a scoping project and then add dev and production as monitored projects.
04:15
While migrating to Google Cloud, Cymbal Superstore will be moving some of its IT expenditure to
04:20
operational expenses, and different departments associated with each application will be responsible for compute and storage costs.
04:27
You’ll need to create a different billing account for each group and link each project to the appropriate account.
04:33
The department lead in Sales and Marketing expresses particular concern about the cost of housing its data warehouse in BigQuery and how to optimize queries and storage.
04:42
You’ll need to set up custom billing budgets and alerts for this department.
04:46
Each department will also need you to set up billing exports that can be used to track charges.


# 8 diagnostic questions
