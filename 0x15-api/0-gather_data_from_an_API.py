#!/usr/bin/python3
"""
A script that fetches and displays an employee's TODO list progress from the
JSONPlaceholder API.

Usage: python3 0-gather_data_from_an_API.py <employee_id>
"""

import os
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Make a GET request to retrieve user's todos
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Filter completed and total tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = todos_data

    # Display employee's todo progress
    print(
        f"Employee {user_data['name']} is done with tasks"
        f"({len(completed_tasks)}/{len(total_tasks)}):"
        )

    # Display completed task titles with newline characters
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        script_name = os.path.basename(__file__)  # Get the script filename
        print(f"Usage: python3 {script_name} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
