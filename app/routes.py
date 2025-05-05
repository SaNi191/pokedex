from . import app
from pokeapi import *
from flask import render_template, flash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rankings')
def rankings():
    return render_template('rankings.html')

# creating route for individual dex entries
@app.route('/pokedex/<name>')
def pokedex(name = "base"):
    
    
    poke_info = get_pokemon(name)

    # poke_info will be false if name is not a valid pokemon
    if name == 'base':
        return render_template('menu.html')
    elif not poke_info:
        flash('Invalid Pokemon!')
        return render_template('menu.html')
    
    # get stats if pokemon is valid
    poke_stats = get_stats(name)

    # using poke_info['name'] fixes id values, passing render_template arguments
    return render_template('dex.html', name = poke_info['name'].capitalize(), stats = poke_stats)

