# Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau contenant uniquement les éléments uniques du tableau d'origine.

print("")
print (f'{"Exo n°15" :=^40}')
print("")
print("Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau contenant uniquement les éléments uniques du tableau d'origine.")
print("")
print("Réponse:")
print("")

import numpy as np

def f(a):
    return np.unique(a)

array = np.array([1, 6, 5, 3, 5, 6, 2, 5, 6, 7, 4, 3, 5])

print("Tableau brut :", array)
print("")

print("Eléments uniques du tableau :", f(array))

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")