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
