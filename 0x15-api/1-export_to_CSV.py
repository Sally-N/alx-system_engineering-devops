#!/usr/bin/python3
"""Exports csv file"""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    baseurl = "https://jsonplaceholder.typicode.com/"
    employee_url = f'{baseurl}users/{employee_id}'
    employee_todos_url = f'{baseurl}users/{employee_id}/todos'

    # Get employee info
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Get employee todos
    response_todos = requests.get(employee_todos_url)
    todos_data = response_todos.json()

    # Tasks
    for task in todos_data:
        task_status = task['completed']
        user_id = task['userId']
        task_title = task['title']

    # Csv
    filename = f"{employee_id}.csv"
    csvdata = [user_id, employee_name, task_status, task_title]
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvdata)
