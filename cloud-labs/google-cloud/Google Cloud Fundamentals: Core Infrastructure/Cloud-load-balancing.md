Previously, we explored how virtual machines can autoscale to respond to changing loads.

But how do your customers get to your application when it might be provided by four VMs one moment, and by 40 VMs at another?

That’s done through Cloud Load Balancing.

The job of a load balancer is to distribute user traffic across multiple instances of an application.

By spreading the load, load balancing reduces the risk that applications experience performance issues.

Cloud Load Balancing is a fully distributed, software-defined, managed service for all your traffic.

And because the load balancers don’t run in VMs that you have to manage, you don’t have to worry about scaling or managing them.

You can put Cloud Load Balancing in front of all of your traffic: HTTP or HTTPS, other TCP and SSL traffic, and UDP traffic too.

Cloud Load Balancing provides cross-region load balancing, including automatic multi-region failover, which gently moves traffic in fractions if backends become unhealthy.

Cloud Load Balancing reacts quickly to changes in users, traffic, network, backend health, and other related conditions.

And what if you anticipate a huge spike in demand?

Say, your online game is already a hit; do you need to file a support ticket to warn Google of the incoming load?

No.

No so-called “pre-warming” is required.

Google Cloud offers a range of load balancing solutions that can be classified based on the OSI model layer they operate at and their specific functionalities.

Application Load Balancers operate at the application layer and are designed to handle HTTP and HTTPS traffic,

making them ideal for web applications and services that require advanced features like content-based routing and SSL/TLS termination.

Application Load Balancers operate as reverse proxies, distributing incoming traffic across multiple backend instances based on rules you define.

They are highly flexible and can be configured for both internet-facing (external) and internal applications.

Network Load Balancers operate at the transport layer and efficiently handle TCP, UDP, and other IP protocols.

They can be further classified into two types: Proxy Network Load Balancers also function as reverse proxies, terminating client connections and establishing new ones to backend services.

They offer advanced traffic management capabilities and support backends located both on-premises and in various cloud environments.

Unlike proxy Network Load Balancers, passthrough Network Load Balancers do not modify or terminate connections.

Instead, they directly forward traffic to the backend while preserving the original source IP address.

This type is well-suited for applications that require direct server return or need to handle a wider range of IP protocols.
