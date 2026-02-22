In this section of the course, we’re going to explore how Google Compute Engine works with a focus on virtual networking.

Many users start with Google Cloud by defining their own virtual private cloud inside their first Google Cloud project or by starting with the default virtual private cloud.

So, what is a virtual private cloud?

A virtual private cloud, or VPC, is a secure, individual, private cloud-computing model hosted within a public cloud – like Google Cloud!

On a VPC, customers can run code, store data, host websites, and do anything else they could

do in an ordinary private cloud, but this private cloud is hosted remotely by a public cloud provider.

This means that VPCs combine the scalability and convenience of public cloud computing with the data isolation of private cloud computing.

VPC networks connect Google Cloud resources to each other and to the internet.

This includes segmenting networks, using firewall rules to restrict access to instances, and creating static routes to forward traffic to specific destinations.

Here's something that tends to surprise a lot of new Google Cloud users: Google VPC networks are global.

They can also have subnets, which is a segmented piece of the larger network, in any Google Cloud region worldwide.

Subnets can span the zones that make up a region.

This architecture makes it easy to define network layouts with global scope.

Resources can even be in different zones on the same subnet.

The size of a subnet can be increased by expanding the range of IP addresses allocated to it, and doing so won’t affect virtual machines that are already configured.

For example, let’s take a VPC network named vpc1 that has two subnets defined in the asia-east1 and us-east1 regions.

If the VPC has three Compute Engine VMs attached to it, it means they’re neighbors on the same subnet even though they’re in different zones.

This capability can be used to build solutions that are resilient to disruptions yet retain a simple network layout.
