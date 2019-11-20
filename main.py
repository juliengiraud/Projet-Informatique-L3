# Ignore  the warnings
#import warnings
#warnings.filterwarnings('always')
#warnings.filterwarnings('ignore')

# data visualisation and manipulation
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#from matplotlib import style
#import seaborn as sns

# encodage des mots en Int
#from numpy import array
#from numpy import argmax
#from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import OneHotEncoder
 
#configure
# sets matplotlib to inline and displays graphs below the corressponding cell.
#%matplotlib inline  
#style.use('fivethirtyeight')
#sns.set(style='whitegrid',color_codes=True)

#model selection
#from sklearn.decomposition import NMF
#from sklearn.model_selection import train_test_split
#from sklearn.model_selection import KFold
#from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,roc_auc_score
#from sklearn.metrics import mean_absolute_error
#from sklearn.model_selection import GridSearchCV
#from sklearn.preprocessing import LabelEncoder

#preprocess.
#from keras.preprocessing.image import ImageDataGenerator

#dl libraraies
#import keras
#from keras import backend as K
#from keras.models import Sequential
#from keras.layers import Dense , merge
#from keras.optimizers import Adam,SGD,Adagrad,Adadelta,RMSprop
#from keras.utils import to_categorical
#from keras.utils.vis_utils import model_to_dot
#from keras.callbacks import ReduceLROnPlateau

#from keras.layers.merge import dot
#from keras.models import Model

# specifically for deeplearning.
#from keras.layers import Dropout, Flatten,Activation,Input,Embedding
#from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
#import tensorflow as tf
#import random as rn
#from IPython.display import SVG
 
# specifically for manipulating zipped images and getting numpy arrays of pixel values of images.
#import cv2 # erreur import
#import numpy as np  
#from tqdm import tqdm
#import os                   
#from random import shuffle  
#from zipfile import ZipFile
#from PIL import Image

#TL pecific modules
#from keras.applications.vgg16 import VGG16

# pour parser le fichier train.json
import json









with open('train.json', 'r') as f:
    datas = json.load(f) # id, cuisine, ingredients[]

csv = []
occurence = dict()
total_plats = dict()
total_ingredients = dict()

for data in datas:
    nb_ingredients = len(data)
    for ingredient in data['ingredients']:
        cuisine = data['cuisine']
        id = str(data['id'])
        
        # Ajout de la ligne id-cuisine-ingredient
        tmp = dict()
        tmp['id'] = id
        tmp['cuisine'] = cuisine
        tmp['ingredient'] = ingredient
        csv.append(tmp)
        
        # Comptage de l'occurence
        if not cuisine in occurence:
            occurence[cuisine] = dict()
        if not ingredient in occurence[cuisine]:
            occurence[cuisine][ingredient] = 0
        occurence[cuisine][ingredient] += 1
        
        # Comptage du nombre d'ingredients de chaque plat
        if not id in total_ingredients:
            total_ingredients[id] = 0
        total_ingredients[id] += 1
        
    # Comptage du nombre de plats par type de cuisine
    if not cuisine in total_plats:
        total_plats[cuisine] = 0
    total_plats[cuisine] += 1

# Ajout des occurences/total_plats dans le CSV
for ligne in csv:
    cuisine = ligne['cuisine']
    ingredient = ligne['ingredient']
    id = ligne['id']
    occ = occurence[cuisine][ingredient]
    ingrs = total_ingredients[id]
    pls = total_plats[cuisine]
    poids1 = 1 / ingrs
    poids2 = occ / pls
    poids3 = 1 / pls
    
    ligne['occurence'] = occ
    ligne['ingredients_plat'] = ingrs
    ligne['recettes_cuisine'] = pls
    ligne['poids_ingredient_recette'] = poids1 # poids de l'ingrédient dans la recette
    ligne['poids_ingredient_cuisine'] = poids2 # poids de l'ingrédient dans le type de cuisine
    ligne['poids_cuisine'] = poids3 # poids de la cuisine dans tous les types de cuisines
    #ligne['poids'] = poids # poids final
    
    ligne['val_relation'] = 1

# $ingredients contient tous les ingredients possibles
# $total_plats contient le nombre total de plats de chaque type de cuisine
# $total_ingredients contient le nombre total d'ingrédient de chaque plat

train = pd.DataFrame(csv)










df = train.copy()
print(df.head())
print(total_plats)
print(df['cuisine'].unique())
print(df['ingredient'].unique())










# Creation de la matrix

index = list(df['id'].unique())
columns = list(df['ingredient'].unique())
index = sorted(index)
columns = sorted(columns)

util_df = pd.pivot_table(data = df, values = 'val_relation', index = 'id', columns = 'ingredient')
print("util_df construite avec NaN")
util_df.to_pickle("util_df.pkl")  # where to save it, usually as a .pkl
'''
util_df = util_df.fillna(0)
print("util_df construite avec 0 à la place des NaN")

util_df.to_pickle("util_df.pkl")  # where to save it, usually as a .pkl
# util_df = pd.read_pickle("util_df.pkl")











X = util_df
model = NMF(n_components=6, init='random', random_state=0)

W = model.fit_transform(X)
H = model.components_

W = pd.DataFrame(W, index, ["type_" + str(i+1) for i in range(len(W[0]))])
H = pd.DataFrame(H, ["type_" + str(i+1) for i in range(len(H))], columns)

print(W)
print(H)
# On peut utiliser sklearn mds pour représenter les ingrédients
# et les cuisines sur une carte 2D en calculant les distances











ax = sns.heatmap(W)
ay = sns.heatmap(H)
'''