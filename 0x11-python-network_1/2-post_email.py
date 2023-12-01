#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter
"""

if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    data_dict = {'email': argv[2]}
    data = parse.urlencode(data_dict).encode()
    req = request.Request(argv[1], data=data)

    with request.urlopen(req) as response:
        html = response.read()

    print(html.decode(response.headers.get_content_charset()))
