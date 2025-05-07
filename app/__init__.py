#__init__.py indicates directory is a python package
from flask import Flask
from app.utils.pokeapi import get_ability
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(
        __name__, 
        template_folder='templates'
    )
    print(__name__)
    app.config.from_pyfile('../config.py')
    db = SQLAlchemy()
    db.init_app(app)

    from . import routes
    from . import filters

    return app




