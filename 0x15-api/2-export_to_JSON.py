#!/usr/bin/python3
"""Exports data in a csv format."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = (sys.argv[1])

    baseurl = "https://jsonplaceholder.typicode.com/"
    employee_url = f'{baseurl}users/{employee_id}'
    employee_todos_url = f'{baseurl}users/{employee_id}/todos'

    # Get employee info
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Get employee todos
    response_todos = requests.get(employee_todos_url)
    todos = response_todos.json()

    # Csv
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": employee_name
            } for t in todos]}, jsonfile)
