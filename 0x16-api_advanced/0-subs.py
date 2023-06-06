#!/usr/bin/python3
"""
This script queries the Reddit API
and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given,
the function will return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    If not a valid subreddit, return 0.
    """

    # Set user agent and url
    user_agent = 'Google Chrome Version 114.0.5735.90',
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit),
    headers = {'User-Agent': user_agent},
    response = requests.get(url, headers=headers, allow_redirects=False)
    r = response.json()

    try:
        return r.get('data').get('subscribers')

    except Exception:
        return 0
