# Objective

# Tools Used

# Steps

# Challenges

# Key Takeaways


# Google Cloud Platform: CLI Foundations & Resource Management

## 📝 Executive Summary
This project marks my inaugural hands-on experience with the **Google Cloud Platform (GCP)**. Through the Google Skills Boost environment, I transitioned from manual GUI management to programmatic cloud administration. This lab focused on the `gcloud` SDK, resource scoping (Regions & Zones), and advanced command-line filtering techniques.

---

## 🛠️ Technical Competencies
* **CLI Administration:** Mastering the `gcloud` tool suite for resource lifecycle management.
* **Cloud Infrastructure:** Provisioning Compute Engine instances via terminal.
* **Data Parsing:** Utilizing flags like `--filter` to extract specific metadata from complex cloud environments.
* **Security Auditing:** Inspecting VPC Firewall rules and network protocols.

---

## 🚀 Lab Workflow & Execution

### 1. Environment Initialization
Before deploying resources, I established a persistent environment in the **Cloud Shell**. This involved setting global configurations to ensure all resources were deployed within the same geographic boundaries.



```bash
# Setting the default compute region and zone
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a

# Storing Project ID and Zone in environment variables for reusability
export PROJECT_ID=$(gcloud config get-value project)
export ZONE=$(gcloud config get-value compute/zone)
