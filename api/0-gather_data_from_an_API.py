#!/usr/bin/python3
"""
Script than return the Todo list with
    name fo employee
    number of done tasks
    number of tasks
"""

import requests
import sys

url = 'https://jsonplaceholder.typicode.com/todos?userId='
url_name = 'https://jsonplaceholder.typicode.com/users?id='


def get_param():
    """substract elemnts from the api"""
    response = requests.get(url + sys.argv[1])
    response_name = requests.get(url_name + sys.argv[1])

    content = [response.json()]
    content_name = [response.json()]

    completed_tasks = 0
    num_of_tasks = 0
    tasks = []

    for t in content:
        if t['completed']:
            completed_tasks += 1
            completed_tasks.append(t['title'])
        tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        content_name[0]['name'], task_completed, total_tasks))
    for t in completed_tasks:
        print('\t' + t)


if __name__ == '__main__':
    get_param()