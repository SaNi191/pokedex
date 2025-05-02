#__init__.py indicates directory is a python package
from flask import Flask

app = Flask(
    __name__, 
    template_folder='templates'
)


@app.route('/')
def home():
    return "<h1>Hello World!</h1>"

@app.route('/rankings')
def rankings():
    return "<h1>Rankings Here!</h1>"

@app.route('/pokedex')
def pokedex():
    return "<h1>PokeDex here</h1>"




