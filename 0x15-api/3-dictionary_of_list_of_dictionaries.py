#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(
                url + "todos",params={"userId": user.get("id")}).json()]
            for user in user_info}, f)
