exo = 27
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer un diagramme en secteurs (camembert) à partir des données suivantes :
categories = ['A', 'B', 'C', 'D'], valeurs = [30, 25, 15, 20]

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

cat = ['A', 'B', 'C', 'D']
val = [30, 25, 15, 20]

plt.close("all")

plt.pie(val, labels = cat)

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')