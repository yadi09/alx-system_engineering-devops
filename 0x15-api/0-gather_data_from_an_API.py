#!/usr/bin/python3
""" returns information about his/her TODO list progress."""

import json
import sys
import urllib.request

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_info = json.loads(urllib.request.urlopen(url + "users/{}".format(
            sys.argv[1])
    ).read().decode('utf-8'))
    todos = json.loads(urllib.request.urlopen(url + "todos?userId={}".format(
        sys.argv[1])
    ).read().decode('utf-8'))
    title = [tit.get('title') for tit in todos if tit.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user_info['name'],
        len(title),
        len(todos)
    ))
    for t in title:
        print("\t" + t)
