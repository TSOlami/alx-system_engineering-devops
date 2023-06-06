#!/usr/bin/python3
"""
This script queries the Reddit API
and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given,
the function will return 0.
"""

import json
import requests


def count_words(subreddit, word_list, after=None, params=None, count=[]):
    """
    """
    if after == "":
        count = [0] * len(word_list)

    # Set user agent and url
    user_agent = {'User-agent': 'tsolami'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        params = {'after': after}
    response = requests.get(
        url,
        headers=user_agent,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)

