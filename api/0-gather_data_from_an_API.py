#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    try:
        employee_id = sys.argv[1]
        user_response = requests.get(url + "users/{}".format(employee_id))
        todos_response = requests.get(url + "todos", params={"userId": employee_id})

        if user_response.status_code == 200 and todos_response.status_code == 200:
            user = user_response.json()
            todos = todos_response.json()

            completed = [todo["title"] for todo in todos if todo.get("completed")]
            print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))

            for complete in completed:
                print("\t {}".format(complete))
        else:
            print("Failed to fetch data for the given employee ID.")
    except requests.RequestException:
        print("API request failed.")
    except ValueError:
        print("Error processing JSON data.")
