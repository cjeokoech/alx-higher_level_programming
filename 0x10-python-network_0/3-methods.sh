#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI ALLOW $1 -L | grep "ALLOw" | cut -d " " -f2-
