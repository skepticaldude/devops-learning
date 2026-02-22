services is setting permissions to a vm without a user, so that it can interact with other cloud services without human intervention.
if i have an app that need to store data in cloud storage but i don't want anyone on the internet to have access to that data, just that particular machine, this is where we create a service account to authenticate that VM to cloud storage 

they are named with an emails address but no password they use cryptographic key to access resources 

you can give them admin access to a Compute Engine’s Instance Admin role here they can view or modify or even delete other VMs .

For example, maybe Alice needs to manage which Google accounts can act as service accounts, while Bob just needs to be able to view a list of service accounts.

Fortunately, in addition to being an identity, a service account is also a resource, so it can have IAM policies of its own attached to it.

This means that Alice can have the editor role on a service account, and Bob can have the viewer role.

This is just like granting roles for any other Google Cloud resource.
