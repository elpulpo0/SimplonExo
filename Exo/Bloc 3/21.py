exo = 21
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer un graphe linéaire des points (x, y) où x = [0, 1, 2, 3, 4] et y = [1, 4, 3, 8, 5].

Réponse:
''')

import matplotlib.pyplot as plt

plt.close("all")
plt.plot([0, 1, 2, 3, 4], [1, 4, 3, 8, 5])
plt.title(f"Exo n°{exo}")
plt.savefig("21.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')


