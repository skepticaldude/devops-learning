#!/bin/bash
# define time
#date "+%Y-%m-%d %H:%M:%S"

USAGE=$(df / | awk 'NR==2 {print $5}')

TIMESTAMP=$(date "+%y-%M-%D %H:%M:%S")

echo "$TIMESTAMP [INFO] Disk usage: $USAGE"

#service check 
if ! systemctl is-active --quiet nginx; then
        echo "$TIMESTAMP [ERROR] Nginx service is down"
fi

