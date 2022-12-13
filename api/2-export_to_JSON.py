#!/usr/bin/python3
"""
Script than extend your Python script to export data
in the json format
"""

import json
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

    attr = []
    for t in content:
        d = {}
        d['task'] = t['title']
        d['completed'] = t['completed']
        d['name'] = content_name[0]['name']
        attr.append(d)

    r = {}
    r['{}'.format(sys.argv[1])] = attr


    JS = json.dumps(r)

    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        f.write(JS)

if __name__ == '__main__':
    gather_data_from_an_api()