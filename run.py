# modules
import json
import numpy as np
from app import create_app
import requests



# response tests

#response = requests.get('https://pokeapi.co/api/v2/pokemon-species/1/').json()
#print(response)
#print(response['name'])

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


