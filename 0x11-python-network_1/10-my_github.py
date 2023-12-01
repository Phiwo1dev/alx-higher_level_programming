#!/usr/bin/python3
"""Takes GitHub credentials (username and password) and uses the GitHub API to display id.
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/user'
    # Builtin shorthand for auth=requests.auth.HTTPBasicAuth('user', 'pass')
    response = get(url, auth=(argv[1], argv[2]))
    print(response.json().get('id'))
