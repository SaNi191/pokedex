#__init__.py indicates directory is a python package
from flask import Flask
from app.utils.pokeapi import get_ability
from flask_sqlalchemy import SQLAlchemy



app = Flask(
    __name__, 
    template_folder='templates'
)

app.config.from_pyfile('../config.py')
db = SQLAlchemy()
db.init_app(app)

from . import routes
from . import filters



