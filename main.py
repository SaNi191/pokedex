# modules
import json
import numpy as np
from app import app
import requests


response = requests.get('https://pokeapi.co/api/v2/pokemon-species/1/').json()

print(response)
print(response['name'])

if __name__ == '__main__':
    app.run(debug=True)


