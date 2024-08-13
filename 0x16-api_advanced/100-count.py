#!/usr/bin/python3
""" recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords """

import requests

header = {'user-agent': 'my-app/0.0.1'}


def count_words(subreddit, word_list, after="", word_dic={}):
    """ prints a sorted count of given keywords """
    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    params = {'limit': 100, 'after': after}

    response = requests.get(url,
                     headers=header,
                     params=params,
                     allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        js = response.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                word_dic[w] += lower.count(w.lower())

    except:
        return None

    count_words(subreddit, word_list, after, word_dic)
