exo = 33
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie le nombre de mots dans cette chaîne (un mot est séparé par un espace).

''')

def fct(phrase):
    return len(phrase)

phraseUser = (input("Ecris une phrase:")).split()

print(f'''

Il y a {fct(phraseUser)} mots dans cette phrase.

{"Fin de l'exo" :=^40}
''')