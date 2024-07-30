#!/usr/bin/python3
""" returns information about his/her TODO list progress."""
import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_info = json.loads(urllib.request.urlopen(url + "users/{}".format(
            sys.argv[1])
    ).read().decode('utf-8'))
    user_id = sys.argv[1]
    uname = user_info.get("username")
    todos = json.loads(urllib.request.urlopen(url + "todos?userId={}".format(
        sys.argv[1])
    ).read().decode('utf-8'))
    title = [tit.get('title') for tit in todos if tit.get('completed') is True]

    with open("{}.csv".format(user_id), "w", newline="") as f:
        obj = csv.writer(f, quoting=csv.QUOTE_ALL)
        [obj.writerow(
            [user_id, uname, task.get("completed"), task.get("title")]
        ) for task in todos]
