#!/usr/bin/python3
"""Returns information about a user's TODO list progress."""

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
    total_tasks = len(todos_data)
    done_tasks = 0
    done_tasks_list = []
    for task in todos_data:
        if task.get('completed') is True:
            done_tasks += 1
            done_tasks_list.append(task)

    # Diplay progress
    print(f'Employee {employee_name} is done with tasks
        ({done_tasks}/{total_tasks}):')

    # Print completed tasks
    for task in done_tasks_list:
        print(f"\t{task['title']}")
