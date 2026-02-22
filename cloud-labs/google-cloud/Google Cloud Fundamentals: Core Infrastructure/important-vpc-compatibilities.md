
Now let’s explore some of the most important Virtual Private Cloud compatibility features.
Much like physical networks, VPCs have routing tables.
VPC routing tables are built-in so you don’t have to provision or manage a router.
They’re used to forward traffic from one instance to another within the same network, across subnetworks, or even between Google Cloud zones, without requiring an external IP address.
Another thing you don’t have to provision or manage for Google Cloud is a firewall.
VPCs provide a global distributed firewall, which can be controlled to restrict access to instances through both incoming and outgoing traffic.
Firewall rules can be defined through network tags on Compute Engine instances, which is really convenient.
For example, you can tag all your web servers with, say, “WEB,” and write a firewall rule saying that traffic on
ports 80 or 443 is allowed into all VMs with the “WEB” tag, no matter what their IP address happens to be.
You’ll remember that VPCs belong to Google Cloud projects, but what if your company has several Google Cloud projects, and the VPCs need to talk to each other?
With VPC Peering, a relationship between two VPCs can be established to exchange traffic.
Alternatively, to use the full power of Identity Access Management (IAM) to control who and what in one project can interact with a VPC in another, you can configu
