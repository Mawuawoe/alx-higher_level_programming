#!/bin/bash
# A Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98

# Check if a URL was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL with the custom header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
