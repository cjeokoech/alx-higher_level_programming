#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            response = response.read().decode("ascii")
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
