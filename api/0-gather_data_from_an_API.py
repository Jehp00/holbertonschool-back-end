#!/usr/bin/python3
"""

"""

import requests
import json

url = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(url)
response_json = response.json()
id = response_json['id']
