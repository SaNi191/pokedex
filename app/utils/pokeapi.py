import requests

POKEAPI_URL = 'https://pokeapi.co/api/v2/'

# api_request(endpoint) will attempt to query pokeapi for desired endpoint, returning False if failed
def api_request(endpoint):
    try:
        response = requests.get(endpoint, timeout = 2)
        response.raise_for_status()
        return response.json()
    except (requests.HTTPError, TimeoutError) as e:
        print(e)
        return False


def get_pokemon(name):
    # call api_request, noting that if any erroneous response occurred the retval will be false
    return api_request(f'{POKEAPI_URL}pokemon/{name}')

def get_stats(name):

    result = api_request(f'{POKEAPI_URL}pokemon/{name}')

    if result:
        return {stat['stat']['name']: stat['base_stat'] for stat in result['stats']}
    else:
        return result


def get_ability(name):
    result = api_request(f'{POKEAPI_URL}pokemon/{name}')

    if not result:
        return result


    ability_result = api_request(result['abilities'][0]['ability']['url'])
    if not ability_result:
        return ability_result


    for entry in ability_result['effect_entries']:
        if entry['language']['name'] == 'en':
            ability_txt = entry['effect']
            break
    
    if not ability_txt:
        ability_txt = 'Ability was not found'
    
    return [ability_result['name'], ability_txt]
