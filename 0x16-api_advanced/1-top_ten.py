#!/usr/bin/python3
"""
This script queries the Reddit API
and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given,
the function will return 0.
"""

import requests


def top_ten(subreddit):
    """
    If not a valid subreddit, return 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Set user agent and url
    user_agent = {'User-agent': 'Google Chrome Version 114.0.5735.90'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    r = response.json()

    try:
        result = r.get('data').get('children')
        for i in result:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
        return
