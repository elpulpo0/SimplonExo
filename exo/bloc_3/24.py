exo = 24
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer un nuage de points à partir de données aléatoires générées par NumPy.

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

x = (np.random.rand(10)*10)+1
y = np.random.rand(10)

plt.close("all")

plt.scatter(x,y)

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')