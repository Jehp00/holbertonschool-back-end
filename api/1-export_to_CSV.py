#!/usr/bin/python3
"""
Script than extend your Python script to export data
in the CSV format
"""

import csv
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

    result = []
    for t in content:
        l = []
        l.append(str(t['userId']))
        l.append(str(content_name[0]['username']))
        l.append(str(t['completed']))
        l.append(str(t['title']))
        result.append(l)

    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        w.writerows(result)


if __name__ == '__main__':
    gather_data_from_an_api()
