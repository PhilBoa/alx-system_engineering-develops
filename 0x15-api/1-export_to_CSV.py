#!/usr/bin/python3
"""
A script fetches an employee's TODO list progress from the JSONPlaceholder
API and exports the data to a CSV file.

Usage: python3 1-export_to_CSV.py <employee_id>
"""

import csv
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


def export_to_csv(tasks, user_data):
    """
    Export tasks to a CSV file.

    Args:
        tasks (list): A list of dictionaries representing tasks.
        user_data (dict): User information.

    Returns:
        None
    """
    user_id = user_data['id']
    user_name = user_data['username']

    # Define the CSV filename based on user_id
    csv_filename = f"{user_id}.csv"

    # Write the data to the CSV file with all values enclosed in double quotes
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write the data rows
        for task in tasks:
            writer.writerow([
                str(user_id),
                user_name,
                str(task['completed']),
                task['title']
                ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        script_name = os.path.basename(__file__)  # Get the script filename
        print(f"Usage: python3 {script_name} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    tasks, user_data = get_employee_todo_progress(employee_id)
    export_to_csv(tasks, user_data)
