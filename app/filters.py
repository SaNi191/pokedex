import os
import requests

from . import app
from app.utils.pokeapi import get_ability, get_sprite


# filter to return pokemon ability information from pokeapi
@app.template_filter('poke_ability')
def poke_ability(txt, selector):
    result = get_ability(txt)
    if not result:
        return 'not found'
    return result[selector]

# filter to return pokemon image address from static folder
# use pokeapi to pull image if not found
@app.template_filter('image_path')
def image_path(txt):

    # create images folder if it doesn't exist
    if not os.path.exists(os.path.join(app.static_folder, 'images')):
        os.makedirs(os.path.join(app.static_folder, 'images'))

    # check if image exists in static folder
    img_path = os.path.join(app.static_folder, 'images', f'{txt}.png')


    if os.path.exists(img_path):
        return f'images/{txt}.png'
    
    
    # retrieve image from pokeapi
    response = get_sprite(txt)
    
    if not response:
        return None
    
    # save image to static folder
    with open(img_path, 'wb') as f:
        f.write(response.content)

    return f'images/{txt}.png'


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