from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# define example
data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
print("\nAvant encodage :\n", data)

e = LabelEncoder()

data = e.fit_transform(data)
print("\nAprès encodage :\n", data)

data = e.inverse_transform(data)
print("\nAprès décodage :\n", data)

'''

with open('train.json', 'r') as f:
    datas = json.load(f) # id, cuisine, ingredients[]

csv = []
for data in datas:
    for ingredient in data['ingredients']:
        tmp = dict()
        tmp['id'] = str(data['id'])
        tmp['cuisine'] = data['cuisine']
        tmp['ingredient'] = ingredient
        csv.append(tmp)

for i in range(50):
    print(csv[i])
'''