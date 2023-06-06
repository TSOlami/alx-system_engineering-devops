#!/usr/bin/python3
"""
This script queries the Reddit API
and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given,
the function will return 0.
"""

import requests


def count_words(subreddit, word_list, after=None, params=None, word_counts={}):
    """
    If not a valid subreddit, return 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Set user agent and url
    user_agent = {'User-agent': 'Google Chrome Version 114.0.5735.90'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        params = {'after': after}
    response = requests.get(
        url,
        headers=user_agent,
        params=params,
        allow_redirects=False)
    data = response.json()

    if response.status_code != 200:
        print('None')
        return
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if title.count(word) > 0 and word not in word_counts:
                word_counts[word] = title.count(word)
            elif title.count(word) > 0 and word in word_counts:
                word_counts[word] += title.count(word)
    if data['data']['after']:
        count_words(subreddit, word_list, data['data']['after'], word_counts)
    else:
        sorted_counts = sorted(word_counts.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')
