#!/usr/bin/python3
"""recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """ function of recurse """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after}

    try:
        response = requests.get(url,
                                headers=header,
                                params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None

    except Exception as ee:
        return None
