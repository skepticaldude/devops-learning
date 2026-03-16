# Reliable Cloud Infrastructure: Design and Process — Course Introduction

**Instructors:**
- Philipp Maier — Course Developer, Google
- Stephanie Wong — Developer Advocate, Google

Welcome to the **Reliable Cloud Infrastructure: Design and Process** course.

This course focuses on **cloud architecture, system design, and operational processes** when building applications on **Google Cloud**.

---

# The Role of a Cloud Architect

A **Cloud Architect** determines which cloud services should be used to most effectively build and operate applications.

However, this is not a simple task.

Many cloud services appear interchangeable, and multiple services can often solve the same problem. The architect's job is to **evaluate options and choose the best solution** based on requirements and constraints.

A common joke about architects is:

> "Architects draw rectangles and connect them with arrows."

While humorous, this actually represents an important step in **designing complex systems**.

---

# Course Focus

This course is **not about implementing specific Google Cloud features**.

Instead, it focuses on:

- Architecture
- System design
- Decision-making processes

During the course, you will work on **designing and architecting a case study application**.

---

# Requirements Gathering

Every software project begins with understanding:

- What the software should do
- Who the users are
- Why the system is important

This phase is known as **requirements gathering**.

Once the requirements are understood, architects can begin designing the system.

---

# System Decomposition

In software architecture, large systems are broken into smaller components.

This process is called **decomposition**.

Modern cloud systems often follow a **microservices architecture**, where applications are divided into smaller independent services.

---

# Microservices Architecture

Microservices are an architectural style that breaks large applications into **independent services**, each responsible for a specific function.

Characteristics of microservices:

- Each service has a **specific responsibility**
- Services can operate **independently**
- Applications are composed of multiple **interacting microservices**

To fulfill a single user request, one service may call several **internal microservices** to produce the final response.

Microservices impact important aspects of development such as:

- Development speed
- Deployment flexibility
- Monitoring and observability

---

# Choosing the Right Cloud Services

Selecting the right services is a critical architectural decision.

For example, architects must decide which **storage systems** to use:

- Relational databases
- NoSQL databases
- Data warehouses

They must also choose the **compute platform**, such as:

- Virtual Machines
- Kubernetes clusters
- Managed platforms like **App Engine**

Each option has advantages and trade-offs depending on system requirements.

---

# Designing for Reliability

Google Cloud provides many services designed to improve system reliability.

Key design considerations include:

- Availability
- Durability
- Cost optimization
- Disaster recovery

Understanding the application requirements allows architects to select services that **meet reliability goals while controlling costs**.

---

# Security Considerations

A common security principle is:

> "Security is not icing on the cake — it is baked into the cake."

Security should be considered **from the beginning of system design**, not added later.

Security in cloud systems follows a **shared responsibility model**.

### Google Cloud Responsibilities
Google secures the underlying infrastructure, including:

- Physical hardware
- Data center facilities
- Core infrastructure

### Customer Responsibilities
Customers are responsible for securing:

- Network configurations
- Storage services
- Virtual machines
- Application logic

Proper system design ensures security requirements are **built into the architecture**.

---

# Monitoring and Observability

Once a system is deployed, it must be monitored to ensure it meets its **service objectives**.

Google Cloud provides multiple monitoring tools, including:

- Dashboards
- Logging
- Error reporting
- Distributed tracing

Monitoring allows teams to measure whether the system is meeting its **performance and reliability goals**.

---

# Learning Path Context

This course is part of the **Google Cloud Infrastructure learning path**, designed for IT professionals responsible for:

- Deploying applications
- Migrating systems to the cloud
- Operating cloud infrastructure
- Maintaining production systems

---

# Course Prerequisites

This course assumes prior knowledge from one of the following:

- **Architecting with Google Compute Engine**
- **Architecting with Google Kubernetes Engine**

It is **not intended as a beginner introduction to Google Cloud**.

---

# Course Structure

The course includes:

- Lectures
- Design activities
- Hands-on labs

Students are encouraged to spend significant time on **design assignments**, because architecture often involves multiple valid solutions.

There is rarely a single correct answer — instead, architects must **weigh trade-offs and choose the best design based on requirements**.

---

# Course Modules

In addition to this introduction, the course contains **nine modules**.

The course will guide you through:

1. Designing a **microservices-based case study application**
2. Using **Google Cloud DevOps and automation tools**
3. Choosing the **appropriate storage services**
4. Designing **network architectures for cloud and hybrid environments**
5. Selecting the **best deployment platforms**
6. Designing systems for **reliability**
7. Designing systems for **security**
8. Monitoring applications and evaluating performance

---

# Key Takeaway

Cloud architecture is about **balancing trade-offs**.

Architects must evaluate:

- technical requirements
- business constraints
- cost
- security
- reliability

The goal is to design the **best possible system for the problem at hand**.
