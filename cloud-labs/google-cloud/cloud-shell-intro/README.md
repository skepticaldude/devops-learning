# Google Cloud Lab: CLI Foundations & Compute Provisioning

# Objective
The primary goal of this lab was to transition from the Google Cloud Console (GUI) to the **gcloud CLI**. I aimed to master the fundamental commands required to configure a cloud environment, provision virtual infrastructure, and perform advanced data filtering to manage cloud resources at scale.

# Tools Used
* **Google Cloud Platform (GCP):** The core cloud ecosystem.
* **Cloud Shell:** A browser-based command-line environment pre-loaded with the SDK.
* **gcloud CLI:** The primary command-line tool for creating and managing Google Cloud resources.
* **Linux Environment:** Utilized Bash commands and environment variables to streamline workflows.

# Steps
1.  **Environment Authentication:** Initialized the session by authorizing Cloud Shell and verifying the active account and project configurations using `gcloud auth list`.
2.  **Geographic Scoping:** Configured the global infrastructure context by setting the default **Region** and **Zone** to ensure resource proximity.
3.  **Variable Management:** Created and exported environment variables (`$PROJECT_ID` and `$ZONE`) to automate command arguments and reduce manual input errors.
4.  **Resource Deployment:** Provisioned a Google Compute Engine (GCE) virtual machine named `gcelab2` using the `e2-medium` machine type via the `gcloud compute instances create` command.
5.  **Output Filtering:** Executed complex queries using the `--filter` flag to isolate specific VM instances and audit firewall rules based on network protocols (e.g., ICMP/Ping rules).



# Automation: The Bash Script
To demonstrate the transition from manual commands to automation, I have compiled the lab steps into a reusable Bash script. This script automates the configuration and VM deployment process.

```bash
#!/bin/bash
# GCP Infrastructure Automation Script

echo "Starting Environment Configuration..."

# 1. Set Project Variables
export PROJECT_ID=$(gcloud config get-value project)
export ZONE="us-central1-a" # Change as needed

# 2. Configure gcloud defaults
gcloud config set compute/zone $ZONE

# 3. Deploy Compute Instance
echo "Deploying VM Instance: gcelab2..."
gcloud compute instances create gcelab2 \
    --machine-type e2-medium \
    --zone $ZONE

# 4. Verify Deployment with Filtering
echo "Verifying Instance Status..."
gcloud compute instances list --filter="name=('gcelab2')"

echo "Deployment Complete."
