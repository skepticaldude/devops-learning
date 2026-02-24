There are four primary storage classes in Cloud Storage.

The first is Standard Storage.

Standard Storage is considered best for frequently accessed, or “hot,” data.

It’s also great for data that’s stored for only brief periods of time.

The second storage class is Nearline Storage.

This is best for storing infrequently accessed data, like reading or modifying data on average once a month or less.

Examples might include data backups, long-tail multimedia content, or data archiving.

The third storage class is Coldline Storage.

This is also a low-cost option for storing infrequently accessed data.

However, as compared to Nearline Storage, Coldline Storage is meant for reading or modifying data, at most, once every 90 days.

And the fourth storage class is Archive Storage.

This is the lowest-cost option, used ideally for data archiving, online backup, and disaster recovery.

It’s the best choice for data that you plan to access less than once a year,

because it has higher costs for data access and operations and a 365-day minimum storage duration.

Although each of these four classes has differences, it’s worth noting there are several characteristics that apply across all of these storage classes.

These include: Unlimited storage with no minimum object size requirement, worldwide accessibility and locations, low latency and high durability, a

uniform experience, which extends to security, tools, and APIs, and geo-redundancy if data is stored in a multi-region or dual-region.

This means placing physical servers in geographically diverse data centers to protect against catastrophic events and natural disasters, and load-balancing traffic for optimal performance.

Cloud Storage also provides a feature called Autoclass, which automatically transitions objects to appropriate storage classes based on each object's access pattern.

The feature moves data that is not accessed to colder storage classes to reduce storage cost and moves data that is accessed to Standard storage to optimize future accesses.

Autoclass simplifies and automates cost saving for your Cloud Storage data.

Cloud Storage has no minimum fee because you pay only for what you use, and prior provisioning of capacity isn’t necessary.

And from a security perspective, Cloud Storage always encrypts data on the server side, before it’s written to disk, at no additional charge.

Data traveling between a customer’s device and Google is encrypted by default using HTTPS/TLS, which is Transport Layer Security.

Regardless of which storage class you choose, there are several ways to bring data into Cloud Storage.

Many customers simply carry out their own online transfer using gcloud storage, which is the Cloud Storage command from the Cloud SDK.

Data can also be moved in by using a drag and drop option in the Cloud Console, if accessed through the Google Chrome web browser.

But what if you have to upload terabytes or even petabytes of data?

Storage Transfer Service enables you to import large amounts of online data into Cloud Storage quickly and cost-effectively.

The Storage Transfer Service lets you schedule and manage batch transfers to Cloud Storage from another cloud provider, from a different Cloud Storage region, or from an HTTP(S) endpoint.

And then there is the Transfer Appliance, which is a rackable, high-capacity storage server that you lease from Google Cloud.

You connect it to your network, load it with data, and then ship it to an upload facility where the data is uploaded to Cloud Storage.

You can transfer up to a petabyte of data on a single appliance.

Cloud Storage’s tight integration with other Google Cloud products and services means that there are many additional ways to move data into the service.

For example, you can import and export tables to and from both BigQuery and Cloud SQL.

You can also store App Engine logs, Firestore backups, and objects used by App Engine applications, like images.

Cloud Storage can also store instance startup scripts, Compute Engine images, and objects used by Compute Engine applications.
