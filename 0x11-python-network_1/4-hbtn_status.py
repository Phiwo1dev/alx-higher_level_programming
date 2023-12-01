#!/usr/bin/python3
"""Uses requests packages, fetches https://alx-intranet.hbtn.io/status.
"""

if __name__ == "__main__":
    from requests import get

    response = get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(
        type(response.text), response.text))
