#!/usr/bin/python3
"""
This script queries the Reddit API
and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given,
the function will return 0.
"""


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    from requests import get

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print(None)
        return None

    try:
        js = r.json()

    except ValueError:
        print(None)
        return None

    try:

        data = js.get("data")
        children = data.get("children")
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))

    except:
        print(None)
