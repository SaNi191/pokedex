#__init__.py indicates directory is a python package
from flask import Flask

def init_app():
    app = Flask(__name__)
    
    return app


