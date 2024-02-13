#!/usr/bin/python3
"""task 0"""
from requests import get


def number_of_subscribers(subreddit):
    user = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/dev/api/r/{}/about.json".format(subreddit)
    with get(url, headers=user, allow_redirects=False) as page:
        if page.status_code >= 300:
            return 0
        data = page.json()
        return data["data"]["subscribers"]
