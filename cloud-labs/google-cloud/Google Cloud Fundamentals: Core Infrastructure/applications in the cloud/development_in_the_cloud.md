Many applications contain event-driven parts.

For example, an application that lets users upload images.

When that event takes place, the image might need to be processed in a few different ways, like converting

the image to a standard format, converting a thumbnail into different sizes, and storing each new file in a repository.

This function could be integrated into the application, but then you’d have to provide compute resources for it–whether it happens once a millisecond or once a day.

With Cloud Run functions, you write a single-purpose function that completes the necessary image manipulations and then arrange for it to automatically run whenever a new image is uploaded.

> Cloud Run functions is a lightweight, event-based, asynchronous compute solution that allows you to create small, single-purpose functions that respond to cloud events, without the need to manage a server or a runtime environment.

These functions can be used to construct application workflows from individual business logic tasks.

Cloud Run functions can also connect and extend cloud services.

You’re billed to the nearest 100 milliseconds, but only while your code is running.

Cloud Run functions supports writing source code in a number of programming languages.

These include; 
* Node.js
* Python
* Go
* Java,
* .Net Core
* Ruby
* and PHP.

For more information about the supported specific version, refer to the runtimes documentation.

Events from Cloud Storage and Pub/Sub can trigger Cloud Run functions asynchronously, or you can use HTTP invocation for synchronous execution.
