exo = 31
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez un programme qui demande à l'utilisateur de saisir une phrase et affiche le nombre de caractères de cette phrase (en comptant les espaces).

''')

def fct(phrase):
    return len(phrase)

phraseUser = input("Ecris une phrase:")

print(f'''

Il y a {fct(phraseUser)} caractères dans cette phrase, en incluant les espaces.

{"Fin de l'exo" :=^40}
''')