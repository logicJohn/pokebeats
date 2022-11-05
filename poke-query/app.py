import requests
import json
from flask import Flask, jsonify
app = Flask(__name__)

pokemontypes = {
    "type1": None,
    "type2": None
}

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(response.status_code)
print("Pokemon name: " + response.json()['forms'][0]['name'])

f = open("pokedex-return.json", "w")
f.write(json.dumps(response.json(), sort_keys=True, indent=4))
f.close()

f = open("pokemon-type.json", "w")
for n in response.json()['types']:
    print(n['type']['name'])
    if pokemontypes['type1'] == None:
        pokemontypes['type1']= n['type']['name']
    else:
        pokemontypes['type2'] = n['type']['name']
f.write(json.dumps(pokemontypes, sort_keys=True, indent=4))
f.close()


@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/<pokemonName>')
def index2(pokemonName):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonName}"
    response = requests.get(url)
    return "hello"

app.run(host='0.0.0.0', port=81)

