#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -s -i "$1" | grep '^Allow: ' | cut -d : -f 2 | cut -b 2- | head -n 1
