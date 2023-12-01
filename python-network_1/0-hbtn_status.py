#!/usr/bin/python3
"""
fetch https://alu-intranet.hbtn.io/status; display response
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: b'Custom status'")
        print("\t- utf8 content: Custom status")
