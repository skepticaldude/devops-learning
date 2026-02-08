# Google Cloud Skills Boost – Learning Documentation

## Lab Title
**GSP002 – Getting Started with Cloud Shell**

## Learning Track
Google Cloud Skills Boost – Hands-on Labs  
Focus Area: Cloud Foundations | Cloud CLI | Infrastructure Operations

---

## Overview
This lab introduced the use of **Google Cloud Shell** as a command-line environment for managing cloud resources.  
Cloud Shell provides a Debian-based virtual machine with preinstalled tools such as the Google Cloud SDK (`gcloud`), enabling rapid interaction with Compute Engine resources directly from a browser.

The lab emphasized:
- Cloud command-line operations
- VM management through CLI
- Secure SSH connectivity
- Firewall configuration
- Log monitoring and troubleshooting

---

## Key Features Explored
- Browser-based Linux terminal environment
- Persistent home directory (5GB storage)
- Preconfigured authentication to Google Cloud
- Preinstalled developer and infrastructure tools
- Direct Compute Engine integration
- Secure SSH instance access

---

## Technical Skills Applied
- Google Cloud CLI (`gcloud`)
- Linux/Bash command-line operations
- Compute Engine instance management
- Secure Shell (SSH) connectivity
- Firewall rule configuration
- Log monitoring using system tools
- Command output filtering and formatting

---

## Lab Tasks Covered
1. Configuring Cloud Shell Environment
2. Filtering Command-Line Output
3. Connecting to VM Instances
4. Updating Firewall Rules
5. Viewing System Logs
6. Knowledge Validation

---

## How to Run (Command Workflow)
#

### Environment Configuration
```bash
gcloud config list
gcloud auth list
export ZONE=us-central1-a
```

### Environment Configuration
```bash
gcloud config list
gcloud auth list
export ZONE=us-central1-a

```

## Filtering Command-Line Output
```bash
gcloud compute instances list
gcloud compute instances list --filter="name:gcelab2"
gcloud compute instances list --format="table(name,zone,status)"
```
## Connect to Compute Engine VM
```bash
gcloud compute ssh gcelab2 --zone $ZONE

```
after that exit vm session
```bash

exit

```






