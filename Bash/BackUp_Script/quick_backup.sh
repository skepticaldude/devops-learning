#!/bin/bash

# Quick Backup Script
# Author: Moses Ikechukwu
# Date: 2026-02-10
# Description: Creates a compressed backup of a specified directory and stores it in a backup folder with a timestamp.

# Source directory to backup (change this path)
SOURCE_DIR="$HOME/Documents"

# Backup destination directory (change this path)
BACKUP_DIR="$HOME/backups"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Generate timestamp
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Backup file name
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# Create the backup
tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" .

# Print result
echo "Backup of $SOURCE_DIR completed successfully!"
echo "Backup file: $BACKUP_FILE"
