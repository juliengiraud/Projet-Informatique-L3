#### IMPORTS ####

# data visualisation and manipulation
import numpy as np
import pandas as pd

# fichiers
import json




#### Chargement des fichiers ####

# Fichier json d'apprentissage
with open('train.json', 'r') as f:
    datas = json.load(f) # id, cuisine, ingredients[]

# Fichier json dont on cherche les types de cuisines
with open('test.json', 'r') as f2:
    datas2 = json.load(f2) # id, ingredients[]

# Matrices pour la prédiction, contenant les données d'apprentissage et de test
H = pd.read_pickle("H.pkl") # Type en fonction des ingrédients (pas vraiment utile)
W = pd.read_pickle("W.pkl") # Type en fonction des plats (c'est de ça qu'on a besoin)





#### Extraction des données des fichiers ####

csv = []
csv2 = []

for data in datas:
    for ingredient in data['ingredients']:
        # Ajout de la ligne id-cuisine-ingredient
        tmp = dict()
        tmp['id'] = str(data['id'])
        tmp['cuisine'] = data['cuisine']
        tmp['ingredient'] = ingredient
        csv.append(tmp)

for data in datas:
    for ingredient in data['ingredients']:
        # Ajout de la ligne id-ingredient
        tmp = dict()
        tmp['id'] = str(data['id'])
        tmp['ingredient'] = ingredient
        csv2.append(tmp)

dfs = pd.DataFrame(csv) # DataFrame des données Source (d'apprentissage : train.json)
dft = pd.DataFrame(csv2) # DataFrame des données de Test (test.json)





#### Récupération des données extraites ####

cuisines = sorted(list(dfs['cuisine'].unique()))
ingredients = sorted(list(dfs['ingredient'].unique()))
id_plats_train = sorted(list(dfs['id'].unique()))
id_plats_test = sorted(list(dft['id'].unique()))





for i in range(300):
    id = id_plats_train[i]
    tmp1 = dfs.loc[(dfs['id'] == id)]['ingredient']
    tmp2 = dft.loc[(dft['id'] == id)]['ingredient']
    if not tmp1.equals(tmp2):
        print(id)
