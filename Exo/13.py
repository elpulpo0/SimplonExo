# Créez une fonction qui prend un tableau NumPy en entrée et renvoie la somme de ses éléments.

print("")
print (f'{"Exo n°13" :=^40}')
print("")
print("Créez une fonction qui prend un tableau NumPy en entrée et renvoie la somme de ses éléments.")
print("")
print("Réponse:")
print("")

import numpy as np

def f(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum

array = np.arange(1,6)

print("Tableau brut :", array)
print("")

# array = list(array)

print("Somme des éléments du tableau :", f(array))

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")