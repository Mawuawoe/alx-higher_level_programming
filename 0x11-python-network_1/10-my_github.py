#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    URL = "https://api.github.com/user"
    response = get(URL, auth=(username, password))
    json = response.json()

    print(json.get('id'))
