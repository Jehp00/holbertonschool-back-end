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


def gather_data_from_an_api():
    """substract elemnts from the api"""
    response = requests.get(url + sys.argv[1])
    response_name = requests.get(url_name + sys.argv[1])

    content = list(response.json())
    content_name = list(response_name.json())

    completed_tasks = 0
    num_of_tasks = 0
    tasks = []

    for t in content:
        if t['completed']:
            completed_tasks += 1
            tasks.append(t['title'])
        num_of_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        content_name[0]['name'], completed_tasks, num_of_tasks))

    for t in tasks:
        print('\t ' + t)


if __name__ == "__main__":
    gather_data_from_an_api()
