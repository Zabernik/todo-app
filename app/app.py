from flask import Flask, render_template, request, redirect, url_for # type: ignore
from db import init_db, add_task, get_tasks, delete_task, toggle_task, update_task

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    priority = request.form['priority']
    add_task(task, priority)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        new_task = request.form['task']
        update_task(task_id, new_task)
        return redirect(url_for('index'))
    task = next((task for task in get_tasks() if task["id"] == task_id), None)
    return render_template('edit.html', task=task)

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    toggle_task(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
