# Google Cloud Pricing Overview – My Notes

To round off this section of the course, I reviewed Google Cloud’s pricing structure and summarized the key points below.

---

## Per-Second Billing

One of the standout features for me is that Google Cloud offers **per-second billing** for several services.

Google was the first major cloud provider to introduce per-second billing for:

- **Compute Engine** (Infrastructure as a Service – IaaS)
- **Google Kubernetes Engine (GKE)** – container infrastructure
- **Dataproc** – managed big data service (Hadoop equivalent as a service)
- **App Engine Flexible Environment VMs** – Platform as a Service (PaaS)

This means I only pay for exactly what I use, down to the second.

---

## Sustained-Use Discounts

Compute Engine provides **automatically applied sustained-use discounts**.

What this means for me:
- If I run a VM instance for more than **25% of a billing month**,  
- Google automatically applies incremental discounts for the additional time used.

There’s nothing I need to configure — the discount is automatic.

---

## Custom Machine Types

Compute Engine allows me to create **custom virtual machine types**.

This lets me:
- Choose the exact amount of **vCPU**
- Choose the exact amount of **memory**

This flexibility helps me:
- Avoid overprovisioning
- Optimize performance
- Control costs more effectively.

---

## Pricing Calculator

Google provides an **online pricing calculator** that helps estimate costs before deployment.

I can use it to:
- Estimate monthly infrastructure costs
- Adjust configurations before committing
- Plan budgets more accurately

---

## Managing Costs and Avoiding Large Bills

To avoid unexpected charges, Google Cloud allows me to set **budgets and alerts**.

### Budgets

I can define budgets at:
- The **billing account level**
- The **project level**

Budgets can be:
- A fixed amount (e.g., $20,000)
- Based on a percentage of the previous month’s spending

### Alerts

I can configure alerts when spending reaches certain thresholds.

For example:
- Budget: $20,000
- Alert at 90%
- I get notified when spending reaches $18,000

Common alert thresholds:
- 50%
- 90%
- 100%
- Or custom values

This gives me proactive cost visibility.

---

## Reports

Google Cloud Console provides a **Reports tool**.

With it, I can:
- Monitor spending visually
- Track expenditure by project
- Track expenditure by service
- Analyze cost trends

This helps me understand where my money is going.

---

## Quotas (Resource Protection)

Google Cloud also uses **quotas** to prevent overconsumption of resources.

This protects:
- My account
- The broader Google Cloud ecosystem

Quotas are applied at the **project level**.

### Types of Quotas

#### 1. Rate Quotas
- Limit the number of requests in a given time frame
- Automatically reset after a specific period

Example:
- GKE allows **3,000 API calls per project every 100 seconds**
- After 100 seconds, the limit resets

#### 2. Allocation Quotas
- Limit the number of resources I can create

Example:
- Each project is limited to **15 Virtual Private Cloud (VPC) networks** by default

All projects start with the same default quotas, but I can request increases through Google Cloud Support if needed.

---

## Key Takeaways (My Summary)

From my understanding:

- Google Cloud uses **per-second billing**, which ensures cost precision.
- **Sustained-use discounts** automatically reduce costs for long-running workloads.
- **Custom machine types** allow me to optimize both performance and pricing.
- **Budgets, alerts, and reports** help me monitor and control spending.
- **Quotas** protect my projects from accidental or malicious overuse.

Overall, Google Cloud provides strong cost control mechanisms while maintaining flexibility and scalability.
