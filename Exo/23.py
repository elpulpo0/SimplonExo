exo = 23
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer un diagramme à barres à partir des données suivantes : 
categories = ['A', 'B', 'C', 'D', 'E'], valeurs = [25, 30, 15, 20, 10]

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

cat = ['A', 'B', 'C', 'D', 'E']
val = [25, 30, 15, 20, 10]

plt.close("all")

# plt.bar(height=val, x=cat)
plt.bar(cat, val)
plt.xlabel("Catégories")
plt.ylabel("Valeures")

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')