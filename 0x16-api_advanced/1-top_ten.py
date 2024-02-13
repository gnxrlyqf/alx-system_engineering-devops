#!/usr/bin/python3
"""task 1"""
from requests import get


def top_ten(subreddit):
    user = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    with get(url, headers=user, allow_redirects=False) as page:
        if page.status_code >= 300:
            print("None")
        data = page.json()
        try:
            list = data["data"]["children"]
            for post in list:
                print(post["data"]["title"])
        except KeyError:
            print("None")
