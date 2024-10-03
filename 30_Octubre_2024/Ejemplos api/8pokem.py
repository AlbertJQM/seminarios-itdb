import requests
if __name__=='__name__':
    url='https://pokeapi.co/api/v2/pokemon-form/'

    response = requests.get(url)
    if response.status_code==200:
        payload = response.json()
        pokemons = payload.get('result', [])
        if pokemons:
            for pokemon in pokemons:
                name = pokemon ['name']
                print (name)