#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept

# Check if a URL was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send an OPTIONS request to the URL and display the Allow header
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f2-
