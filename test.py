import json
import csv

with open('train.json', 'r') as f1:
    datas = json.load(f1) # id, cuisine, ingredients[]

with open('test.json', 'r') as f2:
    tests = json.load(f2)

class Cuisine():
    def __init__(self, nom):
        self.nom = nom
        self.ingredients = []

    def add(self, ingredient):
        if self.ingredients.count(ingredient) == 0:
            self.ingredients.append(ingredient)

cuisines = []

def containCuisine(tab, nom):
    for elem in tab:
        if elem.nom == nom:
            return True
    return False

# Récupération des noms des cuisines
for data in datas:
    cuisine = data['cuisine']
    if not containCuisine(cuisines, cuisine):
        cuisines.append(Cuisine(cuisine))

# Récupération des ingrédients de chaque cuisine
for cuisine in cuisines:
    for data in datas:
        if data['cuisine'] == cuisine.nom:
            for ingredient in data['ingredients']:
                cuisine.add(ingredient)

for cuisine in cuisines:
    print(cuisine.nom, cuisine.ingredients)
