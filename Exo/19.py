# Créez une fonction qui prend un tableau NumPy de nombres entiers en entrée et renvoie un nouveau tableau contenant uniquement les nombres premiers du tableau d'origine.

print(f'''
{"Exo n°19" :=^40}

Créez une fonction qui prend un tableau NumPy de nombres entiers en entrée et renvoie un nouveau tableau contenant uniquement les nombres premiers du tableau d'origine.

Réponse:
''')

import numpy as np
from sympy import isprime

def f(a):
    result = []
    for i in a:
        if isprime(i):
            result.append(i)
        else:
            pass
    return np.array(result)

array = np.array([156, 67, -59, 30, 71, -578, 61, 29, 586, 6, -77, 37, 4, -396, 5])

print(f'''Tableau brut : {array}

Nombres premiers présents dans le tableau : {f(array)}

{"Fin de l'exo" :=^40}
''')

