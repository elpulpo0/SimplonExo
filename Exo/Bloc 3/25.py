exo = 25
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer une courbe sinusoïdale en utilisant NumPy.

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100) # Tableau de 100 valeures allant de 0 à 2 fois pi 
y = np.sin(x) # Tableau des sinus des valeurs du tableau x

plt.close("all")

plt.plot(x, y)

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')