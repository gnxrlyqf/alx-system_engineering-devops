#!/usr/bin/python3
"""task 100"""
from requests import get


def recurse(subreddit, wlist=[], count=0, after=None):
    """returns hot posts of the sub"""
    user = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    args = {"count": count, "after": after}
    with get(url, params=args, headers=user, allow_redirects=False) as page:
        if page.status_code != 200:
            return None
    data = page.json()
    wlist = list(dict.fromkeys(wlist))

    if count == {}:
         word_count = {word: 0 for word in wlist}

    if not data["data"]["after"]:
        return wlist

    return recurse(subreddit, wlist, data["data"]["count"],
                   data["data"]["after"])
