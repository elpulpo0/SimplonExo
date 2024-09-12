exo = 26
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer deux courbes sur le même graphe à partir des données suivantes :
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.close("all")

plt.plot(x, y1)
plt.plot(x, y2)

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')