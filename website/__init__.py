#__init__.py indicates directory is a python package
from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return "<h1>Hello World!</h1>"




