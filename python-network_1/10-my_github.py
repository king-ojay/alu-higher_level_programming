#!/usr/bin/python3
import requests
import sys

def get_github_user_id(username, token):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        data = response.json()
        return data.get('id')
    else:
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    user_id = get_github_user_id(username, token)
    if user_id is not None:
        print(user_id)
    else:
        print(None)

if __name__ == "__main__":
    main()

