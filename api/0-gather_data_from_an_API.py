#!/usr/bin/python3
import requests
import sys

def fetch_todo_data(employee_id):
    """ Fetches and displays the TODO list progress for a given employee ID. """
    # Define API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user and todos data from the API
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.ok and todos_response.ok:
        user = user_response.json()
        todos = todos_response.json()

        if user:
            # Calculate the number of completed and total tasks
            completed_tasks = [todo for todo in todos if todo['completed']]
            total_tasks = len(todos)

            # Print the formatted output
            print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
            for task in completed_tasks:
                print("\t", task['title'])
        else:
            print("User not found.")
    else:
        print("Failed to fetch data from the API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    emp_id = int(sys.argv[1])
    fetch_todo_data(emp_id)
