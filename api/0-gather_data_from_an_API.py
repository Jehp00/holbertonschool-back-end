#!/usr/bin/python3
"""
Script than return the Todo list with
    name fo employee
    number of done tasks
    total number of tasks
    task title
"""

import json
import requests

url = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(url)
response_json = response.json()
print("Employee {} is done with tasks ({}/{}):".
                format(response_json.EMPLOYEE_NAME,
                       response_json.NUMBER_OF_DONE_TASKS,
                       response_json.TOTAL_NUMBER_OF_TASKS))
