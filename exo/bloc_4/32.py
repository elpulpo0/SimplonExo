exo = 32
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie cette chaîne inversée.

''')

def fct(phrase):
    out_phrase = ""
    for c in phrase:
        out_phrase = c + out_phrase
    return out_phrase

phraseUser = input("Ecris une phrase:")

print(f'''

Voici tout les caractères de la phrase du dernier au premier: {fct(phraseUser)}.

{"Fin de l'exo" :=^40}
''')