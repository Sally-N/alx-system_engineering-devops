#!/usr/bin/python3
"""Exports data in a csv format."""

import csv
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
    todos_data = response_todos.json()

    # Csv
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, employee_name, t.get("completed"), t.get("title")]
        ) for t in todos_data]
