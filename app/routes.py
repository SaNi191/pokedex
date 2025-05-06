from . import app
from .utils.pokeapi import *
from flask import render_template, flash, redirect, url_for, request

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rankings')
def rankings():
    return render_template('rankings.html')

@app.route('/dex_menu', methods=['GET'])
def menu():
    if request.method == 'GET':
        poke_name = request.args.get('name')
        if poke_name:
            return redirect(url_for('pokedex', name = poke_name))

    
    return render_template('menu.html')



# creating route for individual dex entries
@app.route('/pokedex/<name>', methods=['POST', 'GET'])
def pokedex(name = None):
    if not name:
        return redirect(url_for('menu'))
    
    poke_info = get_pokemon(name)

    # poke_info will be false if name is not a valid pokemon
    
    if not poke_info:
        flash('Invalid Pokemon!')
        return redirect(url_for('menu'))
    
    # get stats if pokemon is valid
    poke_stats = get_stats(name)

    # using poke_info['name'] fixes id values, passing render_template arguments
    return render_template('dex.html', name = poke_info['name'].capitalize(), stats = poke_stats)

