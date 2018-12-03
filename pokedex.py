# https://pokeapi.co/

import requests
import json
import random
import re


def pokedex(pokemon):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/").json()

    print('{} (#{})\n'.format(r['name'].capitalize(), r['id']), end='')

    for type in r['types']:
        print(type['type']['name'].capitalize(), end='')
        if type == r['types'][0] and len(r['types']) == 2:
            print('/', end='')
    print()
    print()

    print("Ability:")
    abilities = [ability['ability']['name'] for ability in r['abilities']]
    print(random.choice(abilities).capitalize())

    print('\nBase experience: {}'.format(r['base_experience']))

    print('\nHeight: {} m\n'.format(r['height']/10))

    species = requests.get(r['species']['url']).json()

    print('Pokedex entry:')
    entries = [fl['flavor_text'] for fl in species['flavor_text_entries'] if fl['language']['name'] == 'en']
    p = re.compile(r'[\n]')
    entries = list(set(map(lambda x: re.sub(p, ' ', x), entries)))

    print(random.choice(entries))
    print()

    for stat in r['stats']:
        print('{}: {}'.format(stat['stat']['name'].capitalize(), stat['base_stat']))
    print()

    print("Moveset:")
    moves = [move['move']['name'] for move in r['moves']]
    for n, move in enumerate(random.sample(moves, 4)):
        print('{}. {}'.format(n+1, move.capitalize()))

pokemon = random.randint(1, 803)
pokedex(pokemon)