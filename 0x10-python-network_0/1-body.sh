#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
TEST="$(curl -s -X GET "$1" | grep 'HTTP/[0-9]\.[0-9] 200 OK')"
if [ -n "$TEST" ]; then
    curl -s -X GET "$1"
fi

