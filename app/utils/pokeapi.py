import requests

POKEAPI_URL = 'https://pokeapi.co/api/v2/'

# api_request(endpoint) will attempt to query pokeapi for desired endpoint, returning False if failed
def api_request(endpoint, jsonify = False):
    try:
        response = requests.get(endpoint, timeout = 2)
        response.raise_for_status()
        if jsonify:
            return response.json()
        else:
            return response
    except (requests.HTTPError, TimeoutError) as e:
        print(e)
        return False

# get_pokemon(name) will call api_request to get the pokemon data from pokeapi
def get_pokemon(name):
    # call api_request, noting that if any erroneous response occurred the retval will be false
    return api_request(f'{POKEAPI_URL}pokemon/{name}', True)

# get_stats(name) will call api_request to get the pokemon stats from pokeapi, returning a dictionary of stats
def get_stats(name):

    result = api_request(f'{POKEAPI_URL}pokemon/{name}', True)

    if result:
        return {stat['stat']['name']: stat['base_stat'] for stat in result['stats']}
    else:
        return result

# get_ability(name) will call api_request to get the pokemon ability from pokeapi, returning a list of [name, effect]
def get_ability(name):
    result = api_request(f'{POKEAPI_URL}pokemon/{name}', True)

    if not result:
        return result


    ability_result = api_request(result['abilities'][0]['ability']['url'], True)
    if not ability_result:
        return ability_result


    for entry in ability_result['effect_entries']:
        if entry['language']['name'] == 'en':
            ability_txt = entry['effect']
            break
    
    if not ability_txt:
        ability_txt = 'Ability was not found'
    
    return [ability_result['name'], ability_txt]

# get_sprite(name) will call api_request to get the pokemon sprite from pokeapi, returning a response object
def get_sprite(name):

    result = api_request(f'{POKEAPI_URL}pokemon/{name}', True)

    if not result:
        return result

    sprite_url = result['sprites']['front_default']

    response = api_request(sprite_url, False)
    if not response:
        return False
    
    return response
