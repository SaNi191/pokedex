import requests


def get_species(name):
    return requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{name}').json()


def get_stats(name):
    stats = dict()
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()['stats']

    for stat in result:
        stats.update({stat['stat']['name']: int(stat['base_stat'])})

    return stats