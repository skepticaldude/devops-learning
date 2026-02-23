Many Google Cloud customers want to connect their Google Virtual Private Cloud networks to other networks in their system, such as on-premises networks or networks in other clouds.

There are several effective ways to accomplish this.

One option is to start with a Virtual Private Network connection over the internet and use Cloud VPN to create a “tunnel” connection.

To make the connection dynamic, a Google Cloud feature called Cloud Router can be used.

Cloud Router lets other networks and Google VPC, exchange route information over the VPN using the Border Gateway Protocol.

Using this method, if you add a new subnet to your Google VPC, your on-premises network will automatically get routes to it.

But using the internet to connect networks isn't always the best option for everyone, either because of security concerns or because of bandwidth reliability.

So, a second option is to consider “peering” with Google using Direct Peering.

Peering means putting a router in the same public data center as a Google point of presence and using it to exchange traffic between networks.

Google has more than 100 points of presence around the world.

Customers who aren’t already in a point of presence can work with a partner in the Carrier Peering program to get connected.

Carrier Peering gives you direct access from your on-premises network through a service provider's network to Google

Workspace and to Google Cloud products that can be exposed through one or more public IP addresses.

One downside of peering though, is that it isn’t covered by a Google Service Level Agreement.

If getting the highest uptimes for interconnection is important, using Dedicated Interconnect would be a good solution.

This option allows for one or more direct, private connections to Google.

If these connections have topologies that meet Google’s specifications, they can also be covered by an SLA of up to 99.99%.

Also, these connections can be backed up by a VPN for even greater reliability.

Another option we’ll explore is Partner Interconnect, which provides connectivity between an on-premises network and a VPC network through a supported service provider.

A Partner Interconnect connection is useful if a data center is in a physical location that can't reach

a Dedicated Interconnect colocation facility, or if the data needs don’t warrant an entire 10 Gigabytes per second connection.

Depending on availability needs, Partner Interconnect can be configured to support mission-critical services or applications that can tolerate some downtime.

As with Dedicated Interconnect, if these connections have topologies that meet Google’s specifications, they can be covered by an SLA of up to 99.99%,

but note that Google isn’t responsible for any aspects of Partner Interconnect provided by the third-party service provider, nor any issues outside of Google's network.

And the final option is Cross-Cloud Interconnect.

Cross-Cloud Interconnect helps you establish high-bandwidth dedicated connectivity between Google Cloud and another cloud service provider.

Google provisions a dedicated physical connection between the Google network and that of another cloud service provider.

You can use this connection to peer your Google Virtual Private Cloud network with your network that's hosted by a supported cloud service provider.

Cross-Cloud Interconnect supports your adoption of an integrated multicloud strategy.

In addition to supporting various cloud service providers, Cross-Cloud Interconnect offers reduced complexity, site-to-site data transfer, and encryption.

Cross-Cloud Interconnect connections are available in two sizes: 10 gigabits per second, or 100 gigabits per second.

Choosing a network option depends on your applications and business requirements.

You can assess those requirements by answering three simple questions.

Do any of your on-premises servers or user computers with private addressing need to connect to Google Cloud resources with private addressing?

Do the bandwidth and performance of your current connection to Google services currently meet your business requirements?

And do you already have, or are you willing to install and manage, access and routing equipment in one of Google’s point of presence locations?

If you need private-to-private connectivity and your internet connection meets your business requirements, then building a Cloud VPN is your best bet.

If you don’t need private access and your Internet connection is meeting your business requirements, then you can simply use public IP addresses to connect to Google services.

If you don’t need private address connectivity and your current connection to Google Cloud isn’t performing well, then peering may be your best connectivity option.

Direct Peering is a good option if you already have a footprint in one of Google’s

points of presence, or you’re willing to lease co-location space and install and support routing equipment.

If installing equipment isn’t an option, or you would prefer to work with a service provider

partner as an intermediary to peer with Google, then Carrier Peering is the way to go.

If you need private, high-performance connectivity to Google Cloud, but installing equipment isn’t an option, or you would

prefer to work with a service provider partner as an intermediary, then Partner Interconnect would be the recommended option.

Last but not least, there’s Dedicated Interconnect, which provides you with a private circuit direct to Google.
05:39
This is a good option if you already have a footprint or are willing to lease co-lo space and install and support routing equipment, in a Google point of presence.
