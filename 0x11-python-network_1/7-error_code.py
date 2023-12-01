#!/usr/bin/python3
"""Script sends a request to the URL and displays the body of the response.
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        response = get(argv[1])
        response.raise_for_status()
    except:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
