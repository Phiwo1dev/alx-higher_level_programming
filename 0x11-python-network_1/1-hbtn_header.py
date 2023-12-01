#!/usr/bin/python3
""" sends a request to the URL and displays the value, using urlib and sys.
"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
