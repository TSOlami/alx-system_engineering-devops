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
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Set user agent and url
    user_agent = {'User-agent': 'Google Chrome Version 114.0.5735.90'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    r = response.json()

    try:
        return r.get('data').get('subscribers')

    except Exception:
        return 0
