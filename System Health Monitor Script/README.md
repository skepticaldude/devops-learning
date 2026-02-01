# Project: Linux System Health Monitor Script
Overview
A lightweight Bash-based monitoring utility designed to automate routine system health checks.
This script provides real-time visibility into disk usage and critical service status with automated timestamp logging.

Basically this script checks disk usage and the status of the Nginx service.

## Key Features
Disk Usage Monitoring: Automatically extracts the usage percentage of the root filesystem.

Service Verification: Checks the operational status of the Nginx web server using system controllers.

Automated Logging: Prefixes every output with a standard ISO-style timestamp (YYYY-MM-DD HH:MM:SS) for audit trails.

Error Handling: Implements conditional logic to alert administrators when services are down.

## Technical Skills Applied
Bash Scripting: Developed logic for system inspection and conditional reporting.

Command Substitution: Captured dynamic system values using $() and pipes (df, awk).

Permissions Management: Configured executable rights using chmod.

Logic Flow: Utilized if/else statements and exit codes to differentiate between healthy and critical system states.

## How to Run
Clone the project to your local environment.

Set permissions:

chmod +x monitor.sh

Execute the monitor:

./monitor.sh

## Sample Output

2024-01-26 14:44:17 [INFO] Disk usage: 2%

2024-01-26 14:44:17 [ERROR] Nginx service is down
