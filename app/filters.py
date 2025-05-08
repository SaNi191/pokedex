from . import app
from app.utils.pokeapi import get_ability

@app.template_filter('poke_ability')
def poke_ability(txt, selector):
    result = get_ability(txt)
    if not result:
        return 'not found'
    return result[selector]

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
        
        while ind + num >= 26:
            ind -= 26

        char = alphabet[ind + num]

        

        if txt[index].isupper():
            char = char.upper()
        
        new_txt += alphabet[ind + num]
    return new_txt