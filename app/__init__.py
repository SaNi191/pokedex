#__init__.py indicates directory is a python package
from flask import Flask, render_template
from pokeapi import get_species, get_stats

app = Flask(
    __name__, 
    template_folder='templates'
)

app.config.from_pyfile('../config.py')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rankings')
def rankings():
    return "<h1>Rankings Here!</h1>"

# creating route for individual dex entries
@app.route('/pokedex/<name>')
def pokedex(name = "insert pokemon"):
    poke_info = get_species(name)
    poke_stats = get_stats(name)


    # using poke_info['name'] fixes id values, passing render_template arguments
    return render_template('dex.html', name = poke_info['name'].capitalize(), stats = poke_stats)






