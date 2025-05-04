#__init__.py indicates directory is a python package
from flask import Flask, render_template
from pokeapi import get_pokemon, get_stats, get_ability

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
    return render_template('rankings.html')

# creating route for individual dex entries
@app.route('/pokedex/<name>')
def pokedex(name = "base"):
    if name == 'base':
        return render_template('menu.html')
    
    poke_info = get_pokemon(name)
    poke_stats = get_stats(name)

    

    # using poke_info['name'] fixes id values, passing render_template arguments
    return render_template('dex.html', name = poke_info['name'].capitalize(), stats = poke_stats)


# testing a filter
@app.template_filter('caesar_shift')
def caesar_shift(txt, num=1):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    new_txt = ""
    for index, letter in enumerate(txt.lower()):
        ind = alphabet.index(letter)
        while ind + num > 26:
            ind -= 26
        char = alphabet[ind + num]
        if txt[index].isupper():
            char = char.upper()
        
        new_txt += alphabet[ind + num]
    return new_txt


@app.template_filter('poke_ability')
def poke_ability(txt, selector):
    result = get_ability(txt)
    return result[selector]



