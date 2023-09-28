#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"
curl -s -X POST -d "subject=$SUBJECT&email=$EMAIL" "$1"