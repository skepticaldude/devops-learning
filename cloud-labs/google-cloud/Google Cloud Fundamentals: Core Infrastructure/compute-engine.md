Earlier in the course, we explored infrastructure as a service, or IaaS.

Now let’s explore Google Cloud’s IaaS solution: Compute Engine.

With Compute Engine, users can create and run virtual machines on Google infrastructure.

There are no upfront investments, and thousands of virtual CPUs can run on a system that’s designed to be fast and to offer consistent performance.

Each virtual machine contains the power and functionality of a full-fledged operating system.

This means a virtual machine can be configured much like a physical server: by specifying the amount

of CPU power and memory needed, the amount and type of storage needed, and the operating system.

A virtual machine instance can be created via the Google Cloud console, which is a web-based

tool to manage Google Cloud projects and resources, the Google Cloud CLI, or the Compute Engine API.

The instance can run Linux and Windows Server images provided by Google or any customized versions of these images.

You can also build and run images of other operating systems and flexibly reconfigure virtual machines.

A quick way to get started with Google Cloud is through the Cloud Marketplace, which offers solutions from both Google and third-party vendors.

With these solutions, there’s no need to manually configure the software, virtual machine instances, storage, or network settings, although many of them can be modified before launch if that’s required.

Most software packages in Cloud Marketplace are available at no additional charge beyond the normal usage fees for Google Cloud resources.

Some Cloud Marketplace images charge usage fees, particularly those published by third parties, with commercially licensed software, but they all show estimates of their monthly charges before they’re launched.

At this point, you might be wondering about Compute Engine’s pricing and billing structure.

For the use of virtual machines, Compute Engine bills by the second with a one-minute minimum, and sustained-use discounts start to apply automatically to virtual machines the longer they run.

So, for each VM that runs for more than 25% of a month, Compute Engine automatically applies a discount for every additional minute.

Compute Engine also offers committed-use discounts.

This means that for stable and predictable workloads, a specific amount of vCPUs and memory can be purchased for up to

a 57% discount off of normal prices in return for committing to a usage term of one year or three years.

And then there are Preemptible and Spot VMs.

Let’s say you have a workload that doesn’t require a human to sit and wait for it to finish–such as a batch job analyzing a large dataset.

You can save money, in some cases up to 90%, by choosing Preemptible or Spot VMs to run the job.

A Preemptible or Spot VM is different from an ordinary Compute Engine VM in only

one respect: Compute Engine has permission to terminate a job if its resources are needed elsewhere.

Although savings are possible with preemptible or spot VMs, you'll need to ensure that your job can be stopped and restarted.

Spot VMs differ from Preemptible VMs by offering more features.

For example, preemptible VMs can only run for up to 24 hours at a time, but Spot VMs do not have a maximum runtime.

However, the pricing is, currently the same for both.

In terms of storage, Compute Engine doesn’t require a particular option or machine type to get high throughput between processing and persistent disks.

That’s the default, and it comes to you at no extra cost.

And finally, you’ll only pay for what you need with custom machine types.

Compute Engine lets you choose the machine properties of your instances, like the number of virtual CPUs and the

amount of memory, by using a set of predefined machine types or by creating your own custom machine types.
