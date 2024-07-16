#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the URL, and displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value "I will always be here for PLD"

# Check if a URL was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a POST request to the URL with the specified variables and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
