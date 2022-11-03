import requests
import json

pokemontypes = {
    "type1": None,
    "type2": None
}

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(response.status_code)
print("Pokemon name: " + response.json()['forms'][0]['name'])

f = open("pokedex-return.json", "w")
#f.write(response.text)
#print(json.dumps(response.json(), sort_keys=True, indent=4))
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


url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)
#response = requests.post(url, json = pokemontypes)

print(x.status_code)

