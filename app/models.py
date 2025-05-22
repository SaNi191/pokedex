from flask_sqlalchemy import SQLAlchemy
from . import db

class Ability(db.Model): 
    ability_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    desc = db.Column(db.String(100))
    is_hidden = db.Column(db.Boolean)


class Type(db.Model):
    name = db.Column(db.String(10))


class Pokemon(db.Model):
    dex_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable = False)
    type_1 = db.Column(db.String(10))
    type_2 = db.Column(db.String(10))
    ability = db.Column(db.String(20))
    attack = db.Column(db.Integer, nullable = False)
    defense = db.Column(db.Integer, nullable = False)
    special_def = db.Column(db.Integer, nullable = False)
    special_attack = db.Column(db.Integer, nullable = False)
    speed = db.Column(db.Integer, nullable = False)


