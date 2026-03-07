So now that we have a basic understanding of containers and Kubernetes, let’s talk about Google Kubernetes Engine, or GKE.
00:07
GKE is a Google-hosted managed Kubernetes service in the cloud.
00:12
The GKE environment consists of multiple machines, specifically Compute Engine instances, grouped together to form a cluster.
00:21
You can create a Kubernetes cluster with Kubernetes Engine, but how is GKE different from Kubernetes?
00:27
From the user’s perspective, it’s a lot simpler.
00:30
GKE manages all the control plane components for us.
00:34
It still exposes an IP address to which we send all of our Kubernetes API
00:38
requests, but GKE takes responsibility for provisioning and managing all the control plane infrastructure behind it.
00:46
It also eliminates the need of a separate control plane.
00:51
Node configuration and management depends on the type of GKE mode you use.
00:56
With the Autopilot mode, which is recommended, GKE manages the underlying infrastructure such as node configuration, autoscaling, auto-upgrades, baseline security configurations, and baseline networking configuration.
01:11
With the Standard mode, you manage the underlying infrastructure, including configuring the individual nodes.
01:18
Let’s examine the benefits and functionality of Autopilot in more detail.
01:24
Autopilot is optimized for production.
01:27
Autopilot also helps produce a strong security posture.
01:31
And Autopilot also promotes operational efficiency.
01:34
The GKE Standard mode has the same functionality as Autopilot, but you’re responsible for the configuration, management, and optimization of the cluster.
01:45
Unless you require the specific level of configuration control offered by GKE standard, it’s recommended that you use Autopilot mode.
01:54
You can create a Kubernetes cluster with Kubernetes Engine by using the Google Cloud console or the gcloud command that's provided by the Cloud software development kit.
02:04
GKE clusters can be customized, and they support different machine types, number of nodes, and network settings.
02:12
Kubernetes provides the mechanisms through which you interact with your cluster.
02:17
Kubernetes commands and resources are used to deploy and manage applications, perform administration tasks, set policies, and monitor the health of deployed workloads.
02:28
Running a GKE cluster comes with the benefit of advanced cluster management features that Google Cloud provides.
02:35
These include: Google Cloud's load-balancing for Compute Engine instances, Node pools to designate subsets of nodes within a cluster for additional flexibility, Automatic scaling of your cluster's node instance
02:48
count, Automatic upgrades for your cluster's node software, Node auto-repair to maintain node health and availability, And logging and monitoring with Google Cloud Observability for visibility into your cluster.
03:04
To start up Kubernetes on a cluster in GKE, all you do is run this command: $> gcloud container clusters create k1
