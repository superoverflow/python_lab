from flask import Flask

def create_app():
    app = Flask(__name__)
    from tasks.views import tasks_app
    app.register_blueprint(tasks_app)
    return app