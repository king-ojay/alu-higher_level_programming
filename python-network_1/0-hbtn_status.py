#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    req = urllib.request.Request(url, headers={'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
