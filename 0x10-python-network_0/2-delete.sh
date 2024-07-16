#!/bin/bash
# A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response Check if a URL was provided as an argument Send a DELETE request to the URL and display the body of the response
curl -s -X DELETE "${1}"
