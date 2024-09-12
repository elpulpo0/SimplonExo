# Créez une fonction qui prend deux tableaux NumPy en entrée et renvoie le produit scalaire de ces deux tableaux (dot product).

print("")
print (f'{"Exo n°14" :=^40}')
print("")
print("Créez une fonction qui prend deux tableaux NumPy en entrée et renvoie le produit scalaire de ces deux tableaux (dot product).")
print("")
print("Réponse:")
print("")

import numpy as np

def f(a1, a2):
    result = np.dot(a1, a2)
    return result

array1 = np.arange(1,6)
array2 = np.arange(6,11)

print("Tableau 1 brut :", array1)
print("Tableau 2 brut :", array2)
print("")

print("Produit scalaire de ces deux tableaux :", f(array1, array2))

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")