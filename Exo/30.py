exo = 30
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer un graphique en boîte (boxplot) à partir des données suivantes :
data = [np.random.normal(0, 1, 100), np.random.normal(2, 1, 100), np.random.normal(-3, 2, 100)]

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, 1, 100), np.random.normal(2, 1, 100), np.random.normal(-3, 2, 100)]

plt.close("all")

plt.boxplot(data)

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')