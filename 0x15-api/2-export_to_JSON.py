#!/usr/bin/python3
"""gather data from API"""
from requests import get
from sys import argv
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    user = get("{}/{}".format(url, argv[1]))
    name = user.json().get("username")
    tasks_list = []
    users_tasks = {}
    for task in tasks:
        if task["userId"] == int(argv[1]):
            dict = {
                "task": task["title"],
                "completed": task["completed"],
                "username": user.json()["username"]
            }
            tasks_list.append(dict)
    users_tasks[argv[1]] = tasks_list
    with open(argv[1] + ".json", "w") as file:
        json.dump(users_tasks, file)
