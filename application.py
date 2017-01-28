from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    from tasks.views import tasks_app
    app.register_blueprint(tasks_app)
    db.init_app(app)
    return app