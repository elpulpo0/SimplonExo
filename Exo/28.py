exo = 28
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Tracer une courbe polynomiale à partir des données suivantes :
x = np.linspace(-5, 5, 100)
y = 3 * x**3 + 2 * x**2 - 8 * x + 5

Réponse:
''')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
a = 3 * x**3
b = 2 * x**2
c = 8 * x + 5
y = a + b + c

plt.close("all")

plt.plot(x,a, label="a")
plt.plot(x,b, label="b")
plt.plot(x,c, label="c")
plt.plot(x,y, label="a+b+c")
plt.grid()
plt.legend()

plt.title(f"Exo n°{exo}")
plt.savefig(f"{exo}.png")

print(f'''Le graphique a été sauvegardé : {exo}.png

{"Fin de l'exo" :=^40}
''')