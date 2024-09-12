# Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau où tous les éléments
# inférieurs à 5 sont remplacés par 0 et tous les éléments supérieurs ou égaux à 5 sont remplacés par 1.

print("")
print (f'{"Exo n°18" :=^40}')
print("")
print("Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau où tous les éléments")
print("inférieurs à 5 sont remplacés par 0 et tous les éléments supérieurs ou égaux à 5 sont remplacés par 1.")
print("")
print("Réponse:")
print("")

import numpy as np

def f(a):
    a[a < 5] = 0
    a[a >= 5] = 1
    return a

array = np.array([1, 6, 5, 3, 5, 6, 2, 5, 6, 7, 4, 3, 5])

print("Tableau brut :", array)
print("")

print("Eléments du tableau remplacés par 0 et 1 :", f(array))

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")