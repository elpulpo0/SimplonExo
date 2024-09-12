exo = 22
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer un histogramme à partir de données aléatoires générées par NumPy.

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

datas = (np.random.rand(10)*10)+1

plt.close("all")
plt.hist(datas)
plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')


