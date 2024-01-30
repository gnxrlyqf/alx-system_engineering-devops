#!/usr/bin/python3
"""gather data from API"""
from requests import get
from sys import argv
import json

if __name__ == "__main__":
    users = get("https://jsonplaceholder.typicode.com/users/").json()
    tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    all = {}
    for user in users:
        tasks_list = []
        for task in tasks:
            if task["userId"] == user["id"]:
                dict = {
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"],
                }
                tasks_list.append(dict)
        all[user["id"]] = tasks_list
    with open("todo_all_employees.json", "w") as file:
        json.dump(all, file)
