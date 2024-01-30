#!/usr/bin/python3
"""gather data from API"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    tasks = get("https://jsonplaceholder.typicode.com/todos").json()
    user = get("{}/{}".format(url, argv[1]))
    name = user.json().get('name')
    total = []
    completed = []
    for task in tasks:
        if task.get('userId') == int(argv[1]):
            total.append(task["title"])
            if task.get('completed'):
                completed.append(task["title"])
    string = "Employee {} is done with tasks({}/{}):"
    print(string.format(name, len(completed), len(total)))  
    for task in completed:
        print("\t {}".format(task))
