#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    request = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print("[()] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
