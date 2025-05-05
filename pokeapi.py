import requests

def get_pokemon(name):
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if result.status_code == 404:
        # return False if pokemon is not found
        return False
    return result.json()


def get_stats(name):
    stats = dict()
    result = get_pokemon(name)['stats']

    for stat in result:
        stats.update({stat['stat']['name']: int(stat['base_stat'])})

    return stats


def get_ability(name):
    result = get_pokemon(name)
    if result:
        result = result['abilities']
    else:
        return False
    ability_result = requests.get(result[0]['ability']['url']).json()
    for entry in ability_result['effect_entries']:
        if entry['language']['name'] == 'en':
            ability_txt = entry['effect']
            break
    
    if not ability_txt:
        ability_txt = 'ability not found'
    
    return [result[0]['ability']['name'], ability_txt]
