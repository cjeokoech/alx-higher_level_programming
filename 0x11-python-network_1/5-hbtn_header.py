#!/usr/bin/python3
"""sends a request to the URL and displays the value """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    response = request.headers.get("X-Request-Id")
    print(response)
