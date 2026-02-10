# Quick Backup Script

A simple Bash script to create timestamped backups of a directory. Useful for personal projects or small server automation tasks.

## Features

- Compresses a folder into a `.tar.gz` file.
- Automatically timestamps backup files to prevent overwriting.
- Creates backup directory if it doesn't exist.
- Easy to configure source and backup directories.

## Requirements

- Linux or macOS system
- Bash shell
- `tar` command (usually pre-installed)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/devops-scripts.git
    cd devops-scripts
    ```

2. Make the script executable:
    ```bash
    chmod +x quick_backup.sh
    ```

## Usage

Run the script manually:

```bash
./quick_backup.sh
