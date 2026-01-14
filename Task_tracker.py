#!/usr/bin/env python3
"""
Simple CLI Task Tracker
"""

import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'created': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added (ID: {task['id']})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found")
        return
    
    for task in tasks:
        status = "✓" if task['completed'] else " "
        print(f"{task['id']}. [{status}] {task['description']}")
        print(f"   Created: {task['created']}")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f"✅ Task {task_id} marked as complete")
            return
    print(f"❌ Task {task_id} not found")

def main():
    while True:
        print("\n📋 Task Tracker")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number")
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
