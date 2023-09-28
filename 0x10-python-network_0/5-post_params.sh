#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -d "subject=I WILL ALWAYS BE HERE FOR PLD&email=test@gmail.com" "$1"
