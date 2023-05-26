#!/usr/bin/python3
"""Script that returns information about a user's TODO list progress."""

import requests
import sys

employee_id = int(sys.argv[1])

baseurl = "https://jsonplaceholder.typicode.com/"
employee_url = f'{baseurl}users/{employee_id}'
employee_todos_url = f'{baseurl}todos?userId={employee_id}'

try:
    # Get employee info
    response = requests.get(employee_url)
    employee_data = reponse.json()
    employee_name = employee_data['name']

    # Get employee todos
    response = requests.get(employee_todos_url)
    todos_data = response.json()

    # Tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    # Diplay progress
    print(f'Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):');

    # Print completed tasks
    for task in done_tasks:

        print(f"\t{task['title']}")
