#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """ top ten hot posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=header, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            posts = data['data']['children']
            for i in range(min(10, len(posts))):
                print(posts[i]['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
