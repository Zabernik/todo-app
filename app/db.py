import json
import os

DB_FILE = 'tasks.json'

def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump([], f)

def add_task(task):
    tasks = get_tasks()
    new_task = {"id": len(tasks) + 1, "task": task, "completed": False}
    tasks.append(new_task)
    _save_tasks(tasks)

def get_tasks():
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def delete_task(task_id):
    tasks = get_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    _save_tasks(tasks)

def toggle_task(task_id):
    tasks = get_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
    _save_tasks(tasks)

def _save_tasks(tasks):
    with open(DB_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
