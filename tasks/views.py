from flask import Blueprint

tasks_app = Blueprint('task_app',__name__)

@tasks_app.route('/tasks/getTasks')
def get_tasks():
    return "tasks"