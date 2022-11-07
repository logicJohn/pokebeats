
import requests
import json
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return 'Add a pokemon name to the end of the url\n'

@app.route('/<pokemonName>')
def index2(pokemonName):

    pokemontypes = {
        "name" : None,
        "type1": None,
        "type2": None
    }
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonName}"
    response = requests.get(url)
    print(response.status_code)
    print("Pokemon name: " + response.json()['forms'][0]['name'])

    pokemontypes["name"] = response.json()['forms'][0]['name']

    for n in response.json()['types']:
        print(n['type']['name'])
        if pokemontypes['type1'] == None:
            pokemontypes['type1']= n['type']['name']
        else:
            pokemontypes['type2'] = n['type']['name']
    
    return pokemontypes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

