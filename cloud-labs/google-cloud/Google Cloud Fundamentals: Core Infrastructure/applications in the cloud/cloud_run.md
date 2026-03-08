So far in this course, we’ve provided an introduction to Google Cloud and explored the options and benefits related to using virtual machines, networks, storage, and containers in the Cloud.

In the final section of the course, we’ll turn our attention to developing applications in the Cloud.

### cloud run

We’ll begin with Cloud Run, which is a managed compute platform that runs stateless containers via web requests or Pub/Sub events.

> Cloud Run is serverless. That means it removes all infrastructure management tasks so you can focus on developing applications.
> 
> It’s built on Knative, an open API and runtime environment built on Kubernetes.
> 
> It can be fully managed on Google Cloud, on Google Kubernetes Engine, or anywhere Knative runs.
> 
> Cloud Run is fast.
>
> It can automatically scale up and down from zero almost instantaneously
> it charges only for the resources used, calculated down to the nearest 100 milliseconds, so you‘ll never pay for over-provisioned resources.
>

The Cloud Run developer workflow is a straightforward three-step process.

* First, you write your application using your favorite programming language.
*
* This application should start a server that listens for web requests.
*
* Second, you build and package your application into a container image.
*
* And third, the container image is pushed to Artifact Registry, where Cloud Run will deploy it.

Once you’ve deployed your container image, you’ll get a unique HTTPS URL back.

Cloud Run then starts your container on demand to handle requests, and ensures that all incoming requests are handled by dynamically adding and removing containers.

Because Cloud Run is serverless, it means that you, as a developer, can focus on building your application and not on building and maintaining the infrastructure that powers it.

For some use cases, a container-based workflow is great, because it gives you a great amount of transparency and flexibility.

Sometimes, you’re just looking for a way to turn source code into an HTTPS endpoint, and you

want your vendor to make sure your container image is secure, well-configured and built in a consistent way.

With Cloud Run, you can do both.

You can use a container-based workflow, as well as a source-based workflow.

The source-based approach will deploy source code instead of a container image.

Cloud Run then builds the source and packages the application into a container image.

Cloud Run does this using Buildpacks - an open source project.

Cloud Run handles HTTPS serving for you.

That means you only have to worry about handling web requests, and you can let Cloud Run take care of adding the encryption.

The pricing model on Cloud Run is unique; as you only pay for the system resources you use

while a container is handling web requests, with a granularity of 100ms, and when it’s starting or shutting down.

You don’t pay for anything if your container doesn’t handle requests.

Additionally, there is a small fee for every one million requests you serve.

The price of container time increases with CPU and memory.

A container with more vCPU and memory is more expensive.

You can use Cloud Run to run any binary, as long as it’s compiled for Linux sixty-four bit.

Now, this means you can use Cloud Run to run web applications written using popular languages, such as: Java, Python, Node.js, PHP, Go, and C++.

You can also run code written in less popular languages, such as: Cobol, Haskell, and Perl.

As long as your app handles web requests, you’re good to go.
