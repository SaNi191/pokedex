import requests

def get_pokemon(name):
    return requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()

def get_stats(name):
    stats = dict()
    result = get_pokemon(name)['stats']

    for stat in result:
        stats.update({stat['stat']['name']: int(stat['base_stat'])})

    return stats

def get_ability(name):
    result = get_pokemon(name)['abilities']
    ability_result = requests.get(result[0]['ability']['url']).json()
    print(ability_result)
    return [result[0]['ability']['name'], ability_result['effect_entries'][0]['effect']]
