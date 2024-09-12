# Écrivez un programme qui demande à l'utilisateur de saisir un nombre entier positif et affiche tous les nombres de 1 jusqu'à ce nombre (inclus).

import numpy as np

print("")
print (f'{"Exo n°01" :=^40}')
print("")


nbreEntierFromUser = int(input("Saisis un nombre entier positif:"))
nbre = np.arange(0, nbreEntierFromUser + 1, 1)

for val in nbre:
    print(val)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")