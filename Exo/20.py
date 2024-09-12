# Créez un tableau NumPy 2D de taille 3x3 contenant des valeurs entières générées aléatoirement entre 1 et 10.

print(f'''
{"Exo n°20" :=^40}

Créez un tableau NumPy 2D de taille 3x3 contenant des valeurs entières générées aléatoirement entre 1 et 10.

Réponse:
''')

import numpy as np

array = (np.random.rand(3,3)*10)+1

print(f'''{array}

{"Fin de l'exo" :=^40}
''')