As we’ve just seen, with Compute Engine, you can choose the most appropriate machine properties for your instances, like the number

of virtual CPUs and the amount of memory, by using a set of predefined machine types, or by creating custom machine types.

To do this, Compute Engine has a feature called Autoscaling, where VMs can be added to or subtracted from an application based on load metrics.

The other part of making that work is balancing the incoming traffic among the VMs.

Google’s Virtual Private Cloud (VPC) supports several different kinds of load balancing, which we’ll explore shortly.

With Compute Engine, you can in fact configure very large VMs, which are great for workloads such

as in-memory databases and CPU-intensive analytics, but most Google Cloud customers start off with scaling out, not up.

The maximum number of CPUs per VM is tied to its “machine family” and is also constrained by the quota available to the user, which is zone-dependent.

Specifications for currently available VM machine types can be found at cloud.google.com/compute/docs/machine-types
