# https://pokeapi.co/

import requests
import json
import re

with open("sun&moon_pokemon.txt") as f:
    pokemon_list = f.read().split('\n')

pokemon_list[0] = "Bulbasaur"

pokemon_json = {}

for pokemon in range(1, 803):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/").json()
    species = requests.get(r['species']['url']).json()

    name = pokemon_list[pokemon - 1]

    pokedex_number = r['id']
    types = list(reversed([typ['type']['name'] for typ in r['types']]))
    abilities = [ability['ability']['name'] for ability in r['abilities']]
    base_experience = r['base_experience']
    height = r['height']/10

    entries = [fl['flavor_text'] for fl in species['flavor_text_entries'] if fl['language']['name'] == 'en']
    p = re.compile(r'[\n]')
    entries = list(set(map(lambda x: re.sub(p, ' ', x), entries)))

    stats = {stat['stat']['name']: stat['base_stat'] for stat in r['stats']}

    moves = [move['move']['name'] for move in r['moves']]

    pokemon_json[name] = {
                          'Pokedex Number': pokedex_number,
                          'Type': types,
                          'Abilities': abilities,
                          'Experience': base_experience,
                          'Height': height,
                          'Flavor Text': entries,
                          'Stats': stats,
                          'Moves': moves
                         }
    print(name)

with open("pokemon.json", "w") as f:
    json.dump(pokemon_json, f, indent=2)
