import json
import random

class Pokemon:
    def __init__(self, species, level=1, ability="None", moves=[]):
        with open("./Lists of Pokemon/pokemon.json") as f:
            info = json.load(f)

        self.info = info[species]

        self.species = species
        self.number = self.info['Pokedex Number']
        self.type = self.info['Type']
        self.height = self.info['Height']
        self.flavor_text = self.info['Flavor Text']

        self.stats = self.info['Stats']
        self.speed = self.stats['speed']
        self.special_defense = self.stats['special-defense']
        self.special_attack = self.stats['special-attack']
        self.defense = self.stats['defense']
        self.attack = self.stats['attack']
        self.hp = self.stats['hp']

        self.level = level

        self.moves = list(set([move for move in moves if move in self.info['Moves']]))

        if len(self.moves) == 0:
            self.moves.append(random.choice(self.info['Moves']))

        if ability.lower() in self.info['Abilities']:
            self.ability = ability.capitalize()
        else:
            self.ability = random.choice(self.info['Abilities']).capitalize()

    def getPokedexEntry(self):
        return random.choice(self.flavor_text)

    def levelUp(self):
        self.level += 1

    def moveTutor(self, move):
        if len(self.moves) < 4 and move in self.info['Moves'] and move not in self.moves:
            self.moves.append(move)
        elif len(self.moves) == 4:
            print("{} wants to learn {}, but already knows 4 moves.".format(self.species, move))
            self.moveDeleter()
            self.moves.append(move)

    def moveDeleter(self):
        if len(self.moves) > 1:
            print("Which move should be deleted?")
            for n, move in enumerate(self.moves):
                print('{}. {}'.format(n+1, move.capitalize()))
            choice = int(input("Choice: ")) - 1
            self.moves.pop(choice)

    def pokedex(self):
        dex = ''
        dex += self.species + ' ' + f'(#{self.number})'

        dex += '\n' + self.type[0].capitalize()
        if len(self.type) == 2:
            dex += '/' + self.type[1].capitalize()

        dex += '\n\n' + f'Ability: {self.ability}'
        dex += '\n\n' + f'Height: {self.height} m'
        dex += '\n\n' + random.choice(self.flavor_text)
        dex += '\n\nStats:'
        dex += f'\nSpeed:           {self.speed}\nSpecial Defense: {self.special_defense}'
        dex += f'\nSpecial Attack:  {self.special_attack}\nDefense:         {self.defense}'
        dex += f'\nAttack:          {self.attack}\nHP:              {self.hp}\n\n'

        dex += 'Moves:\n'
        for n, move in enumerate(self.moves):
            dex += f'{n+1}. {move.capitalize()}\n'
        return dex
