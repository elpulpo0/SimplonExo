exo = 34
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie une nouvelle chaîne où chaque mot est en majuscules.

''')

def fct(phrase):
    newPhrase = list()
    for mot in phrase:
        newPhrase.append(mot.capitalize())
    return ' '.join(newPhrase)

phraseUser = (input("Ecris une phrase:")).split()

print(f'''

Voici la phrase avec des majuscule à chaque mot: {fct(phraseUser)}.

{"Fin de l'exo" :=^40}
''')