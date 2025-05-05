#__init__.py indicates directory is a python package
from flask import Flask
from pokeapi import get_pokemon, get_stats, get_ability


app = Flask(
    __name__, 
    template_folder='templates'
)

app.config.from_pyfile('../config.py')


from . import routes

# testing a filter
@app.template_filter('caesar_shift')
def caesar_shift(txt, num=1):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    new_txt = ""
    for index, letter in enumerate(txt.lower()):
        if letter not in alphabet:
            new_txt += letter
            continue

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
    if not result:
        return 'not found'
    return result[selector]



