import requests
from bs4 import BeautifulSoup

# For Kanto region only
bulbapedia = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Kanto_Pok%C3%A9dex_number'

# For regional Pokedex
# bulbapedia = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'

pokemon = ''

site = requests.get(bulbapedia).text
b = BeautifulSoup(site, 'lxml')

table = b.find_all('table')[1:-3]

for x in table:
    trow = x.find_all('tr')
    trow.pop(0)

    for row in trow:
        name = row.find_all('td')[3].text[1:-1]
        pokemon += name + '\n'

with open("pokemon1.txt", 'w', encoding = 'utf-8') as f:
    # All Pokemon
    f.write(pokemon[:-1])

    # To remove Melmetal and Meltan 
    # f.write(pokemon[:-17])
