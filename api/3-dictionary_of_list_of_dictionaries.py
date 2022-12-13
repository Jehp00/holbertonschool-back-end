#!/usr/bin/python3
"""
Script than extend your Python script to export data
in the json format
"""

import json
import requests
import sys


url = 'https://jsonplaceholder.typicode.com/todos'
url_usr = 'https://jsonplaceholder.typicode.com/users'


def gather_data_from_an_api():
    """substract elemnts from the api"""

    response = requests.get(url)
    response_usr = requests.get(url_usr)

    content = list(response.json())
    content_usr = list(response_usr.json())

    r = {}
    for u in content_usr:
        attr = []
        for t in content:
            d = {}
            d['name'] = u['name']
            d['task'] = t['title']
            d['completed'] = t['completed']

            if u['id'] == t['userId']:
                attr.append(d)
        r[u['id']] = attr

    JS = json.dumps(r)

    with open('todo_all_employees.json', 'w') as f:
        f.write(JS)


if __name__ == '__main__':
    gather_data_from_an_api()