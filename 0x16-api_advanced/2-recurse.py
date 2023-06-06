#!/usr/bin/python3
"""
This script queries the Reddit API
and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given,
the function will return 0.
"""

import requests


after = None


def recurse(subreddit, hot_list=[]):
    """
    If not a valid subreddit, return 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Set user agent and url
    user_agent = {'User-agent': 'Google Chrome Version 114.0.5735.90'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    global after
    params = {'after': after}
    response = requests.get(
        url,
        headers=user_agent,
        params=params,
        allow_redirects=False)
    r = response.json()

    if response.status_code == 200:
        data = r["data"]["after"]
        if data is not None:
            after = data
            recurse(subreddit, hot_list)
        titles = r["data"]["children"]
        for a_title in titles:
            hot_list.append(a_title["data"]["title"])
        return hot_list
    else:
        return "None"
