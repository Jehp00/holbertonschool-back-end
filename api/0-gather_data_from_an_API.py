#!/usr/bin/python3
"""

"""

import json
import requests

url = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(url)
response_json = response.json()
return("Employee {} is done with tasks\
    ({}/{}):".format(response_json.name, 
    NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
