Let’s begin with Cloud Storage, which is a service that offers developers and IT organizations durable and highly available object storage.

## But what is object storage?

Object storage is a computer data storage architecture that manages data as “objects” and not

as a file and folder hierarchy (file storage), or as chunks of a disk (block storage).

These objects are stored in a packaged format which contains the binary form of the actual data itself, as

well as relevant associated meta-data (such as date created, author, resource type, and permissions), and a globally unique identifier.

These unique keys are in the form of URLs, which means object storage interacts well with web technologies.

Data commonly stored as objects include video, pictures, and audio recordings.

* Cloud Storage is Google’s object storage product.

It allows customers to store any amount of data, and to retrieve it as often as needed.

It’s a fully managed scalable service that has a wide variety of uses.

A few examples include serving website content, storing data for archival and disaster recovery, and distributing large data objects to end users via Direct Download.

Cloud Storage’s primary use is whenever binary large-object storage (also known as a “BLOB”) is needed for online content

such as videos and photos, for backup and archived data and for storage of intermediate results in processing workflows.

Cloud Storage files are organized into buckets.

A bucket needs a globally unique name and a specific geographic location for where it should be stored, and an ideal location for a bucket is where latency is minimized.

For example, if most of your users are in Europe, you probably want to pick a

European location, so either a specific Google Cloud region in Europe, or else the EU multi-region.

The storage objects offered by Cloud Storage are immutable, which means that you do not edit them, but instead a new version is created with every change made.

Administrators have the option to either allow each new version to completely overwrite the older one, or

to keep track of each change made to a particular object by enabling “versioning” within a bucket.

## object versioning in buckets

If you choose to use versioning, Cloud Storage will keep a detailed history of modifications -- that is, overwrites or deletes -- of all objects contained in that bucket.

If you don’t turn on object versioning, by default new versions will always overwrite older versions.

With object versioning enabled, you can list the archived versions of an object, restore an object to an older state, or permanently delete a version of an object, as needed.

In many cases, personally identifiable information may be contained in data objects, so controlling access to stored data is essential to ensuring security and privacy are maintained.

## Using IAM roles and access control lists (ACLs)

Using IAM roles and, where needed, access control lists (ACLs), organizations can conform to security best practices, which require each

user to have access and permissions to only the resources they need to do their jobs, and no more than that.

There are a couple of options to control user access to objects and buckets.

For most purposes, IAM is sufficient.

Roles are inherited from project to bucket to object.

### access control lists

If you need finer control, you can create access control lists.

Each access control list consists of two pieces of information.

The first is a scope, which defines who can access and perform an action.

This can be a specific user or group of users.

The second is a permission, which defines what actions can be performed, like read or write.

Because storing and retrieving large amounts of object data can quickly become expensive, Cloud Storage also offers lifecycle management policies.

For example, you could tell Cloud Storage to delete objects older than 365 days; or to delete objects created before January

1, 2013; or to keep only the 3 most recent versions of each object in a bucket that has versioning enabled.

Having this control ensures that you’re not paying for more than you actually need.
