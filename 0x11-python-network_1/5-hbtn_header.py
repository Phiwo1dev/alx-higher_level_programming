#!/usr/bin/python3
"""Uses requests and sys packages, sends a request to the URL and displays the value of a variable.
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    print(response.headers.get('x-request-id'))
