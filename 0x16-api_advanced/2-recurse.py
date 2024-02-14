#!/usr/bin/python3
"""task 2"""
from requests import get


def recurse(subreddit, hot_list=[], count=0, after=None):
    """returns hot posts of the sub"""
    user = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    args = {"count": count, "after": after}
    with get(url, params=args, headers=user, allow_redirects=False) as page:
        if page.status_code >= 300:
            return None
    data = page.json()
    list = hot_list + [child["data"]["title"]
                       for child in data["data"]["children"]]
    if not data["data"]["after"]:
        return list

    return recurse(subreddit, list, data["data"]["count"],
                   data["data"]["after"])
