# Créez une fonction qui prend un tableau NumPy en entrée et renvoie la moyenne, la médiane et l'écart type de ses éléments.

print("")
print (f'{"Exo n°17" :=^40}')
print("")
print("Créez une fonction qui prend un tableau NumPy en entrée et renvoie la moyenne, la médiane et l'écart type de ses éléments.")
print("")
print("Réponse:")
print("")

import numpy as np

def f(a):
    moyenne = np.mean(a)
    mediane = np.median(a)
    ecart = np.std(a)
    return [moyenne, mediane, ecart]

array = np.array([1, 6, 5, 3, 5, 6, 2, 5, 6, 7, 4, 3, 5])

print("Tableau brut :", array)
print("")

print("Moyenne, médiane et écart type des éléments du tableau :", f(array))

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")