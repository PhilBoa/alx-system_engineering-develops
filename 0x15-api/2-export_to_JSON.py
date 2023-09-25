#!/usr/bin/python3
"""
A script that fetches an employee's TODO list progress from the JSONPlaceholder
API and exports the data to a JSON file.

Usage: python3 2-export_to_JSON.py <employee_id>
"""

import json
import os
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of dictionaries representing tasks.
    """
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Make a GET request to retrieve user's todos
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    return todos_data, user_data


def export_to_json(tasks, user_data):
    """
    Export tasks to a JSON file.

    Args:
        tasks (list): A list of dictionaries representing tasks.
        user_data (dict): User information.

    Returns:
        None
    """
    user_id = user_data['id']
    user_name = user_data['username']

    # Define the JSON filename based on user_id
    json_filename = f"{user_id}.json"

    # Create a list of task dictionaries
    task_list = []
    for task in tasks:
        task_dict = {
            "task": task['title'],
            "completed": task['completed'],
            "username": user_name
        }
        task_list.append(task_dict)

    # Create the JSON object with user_id as the key and the list of tasks
    export_data = {str(user_id): task_list}

    # Write the data to the JSON file
    with open(json_filename, mode='w') as json_file:
        json.dump(export_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        script_name = os.path.basename(__file__)  # Get the script filename
        print(f"Usage: python3 {script_name} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    tasks, user_data = get_employee_todo_progress(employee_id)
    export_to_json(tasks, user_data)
