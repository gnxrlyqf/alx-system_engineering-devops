#!/usr/bin/python3
"""gather data from API"""
from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    user = get("{}/{}".format(url, argv[1]))
    name = user.json().get("username")
    with open(argv[1] + '.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task.get('userId') == int(argv[1]):
                row = [argv[1], name, str(task["completed"]), task["title"]]
                writer.writerow(row)
