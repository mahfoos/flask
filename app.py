from flask import Flask

application = app = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'