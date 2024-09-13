exo = 35
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend un nombre entier en entrée et affiche tous les 
nombres de 1 jusqu'à ce nombre (inclut) en utilisant une boucle "while"

''')

import numpy as np

n = np.array(0,)

def fct1(num):
    num_list = []
    while n <= num:
        num_list.append(n)
    return num_list

def fct2(phrase):
    if phrase == fct1(phrase):
        result = "est"
    else:
        result = "n'est pas"
    return result

phraseUser = input("Ecris un mot:")

print(f'''

{phraseUser} {fct2(phraseUser)} un palindrome.

{"Fin de l'exo" :=^40}
''')