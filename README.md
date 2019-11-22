# Projet

<https://www.kaggle.com/c/whats-cooking/overview>

<https://www.kaggle.com/rajmehra03/cf-based-recsys-by-low-rank-matrix-factorization>

<https://www.kaggle.com/rajmehra03/a-detailed-explanation-of-keras-embedding-layer>

<https://www.kaggle.com/halflings/ingredient-recommender-system>

<https://www.kaggle.com/dipayan/whatscooking-python>

<https://www.kaggle.com/alonalevy/cultural-diffusion-by-recipes>

---

## Conseils du prof

Le prof nous a conseillé de se renseigner sur [l'algorithme t-SNE](https://fr.wikipedia.org/wiki/Algorithme_t-SNE)

Il nous a aussi dit que [sklearn](https://scikit-learn.org/) est une librairie python qui est beaucoup utilisée pour faire du machine learning

## Factorisation de matrix

Nous avons utilisé le code suivant pour factoriser notre matrix

```python
util_df = util_df.fillna(0)
X = util_df
from sklearn.decomposition import NMF
model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(X)
H = model.components_
```

## Prédiction

La lirairie [seaborn.heatmap](http://seaborn.pydata.org/generated/seaborn.heatmap.html) permet de visualiser les types de cuisine selon leur couleur (couleurs proches = cuisines proches)

```python
import seaborn as sns
# reconvertir ax en dataFrame pour remettre les nom de cuisine
ax = sns.heatmap(W)
```

Et si on utilise ce code pour visualiser les ingrédients on verra qu'ils ont des couleurs semblables aux couleurs de leurs cuisines

## Note importante

Dans notre apprentissage nous utilisons l'occurence des ingrédients dans les cuisines, ce qui veut dire qu'un ingrédients utilisé dans beaucoup de plats sur un type de cuisine aura un poids très fort. Le problème c'est que nous n'avons pas le même nombre de plats par type de cuisine ! Ce qui biaise la façon d'interpréter ces données d'occurence. Il faudrait essayer de diviser la valeur d'occurence par le nombre de plats qui contiennent l'ingrédient (ou par le nombre de plats du type de cuisine peut-être ?)
Ou disons que chaque ingrédient a un poid de 1000 au départ, on divise ce 1000 par le nombre d'utilisation de l'ingrédient ce qui donne son nouveau poids, et au final on multiplie les occurence de l'ingrédient par ce poids
Sinon on calcul pour chaque type de cuisine le pourcentage de recettes qui utilise chaque ingrédient et on multiplie son occurence par cette valeur

### Normalisation

Ok en fait il faut normaliser notre façon de compter. Déjà il faut rendre équitable le nombre de recettes par type de cuisine (1), ensuite il faut rendre équitable l'utilisation des ingrédients dans les recettes (2) et enfin il faut prendre en compte la proportion d'utilisation des ingrédients dans un type de cuisine, c'est à dire que plus il y a d'ingrédients différents moins ils sont importants (3)

1. Si un type A de cuisine a 2 fois plus de recettes qu'un type B, il faudrait multiplier toutes les occurences du type B par 2 : compter combien de recettes possède chaque cuisine, prendre le max et pour chaque cuisine multiplier les occurences par nb_de_recettes_de_la_cuisine/max

2. Lors du compte des occurences on ajoute 1 à chaque fois, il faut ajouter 1 / le nombre d'ingrédient de la recette

3. Pour chaque ingrédients il faut prendre en compte sa proportion dans chaque type de cuisine : pour chaque type de cuisine, multiplier l'occurence de chaque ingrédient par (son occurence dans le type de cuisine / somme des occurences d'ingrédients du type de cuisine)

## MAJ du 22/11/2019

Il faut vérifier les données sources, problème de taille de matrice.

On peut utiliser notre model NMF pour obtenir les valeurs d'un nouveau plat (model.transform([valeurs...])).

Est-ce qu'on peut obtenir les coordonnées d'un nouveau plat à la volée ?

On peut enregistrer notre model dans un fichier avec la librairie pickle et donc générer un point en direct à partir d'une nouvelle recette à la soutenance.
