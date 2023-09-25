#!/usr/bin/python3
"""
A script that fetches TODO list progress for all employees from the
JSONPlaceholder API and exports the data in JSON format.

Usage: python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import os
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetch and return an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: User information and list of tasks.
    """
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Make a GET request to retrieve user's todos
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    return user_data, todos_data


def export_data_to_json(data_to_export):
    """
    Export user data and tasks for all employees to a JSON file.

    Args:
        data_to_export (dict): Data to export.

    Returns:
        None
    """
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data_to_export, json_file)


def main():
    # Define the range of employee IDs
    min_employee_id = 1
    max_employee_id = 10

    data_to_export = {}

    for employee_id in range(min_employee_id, max_employee_id + 1):
        user_data, tasks = get_employee_todo_progress(employee_id)
        user_id = user_data['id']
        username = user_data['username']

        data_to_export[str(user_id)] = [
            {
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            } for task in tasks
        ]

    export_data_to_json(data_to_export)


if __name__ == "__main__":
    main()
