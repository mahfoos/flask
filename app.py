from flask import Flask

app = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'