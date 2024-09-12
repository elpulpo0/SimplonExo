exo = 29
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer un diagramme en barres empilées à partir des données suivantes :
categories = ['A', 'B', 'C', 'D']
valeurs1 = [10, 15, 20, 25], valeurs2 = [5, 10, 15, 20]

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

cat = ['A', 'B', 'C', 'D']
val1 = [10, 15, 20, 25]
val2 = [5, 10, 15, 20]

plt.close("all")

plt.bar(cat,val1)
plt.bar(cat,val2)

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')