exo = 35
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie True si cette chaîne est un palindrome 
(c'est-à-dire qu'elle se lit de la même manière de gauche à droite et de droite à gauche), sinon renvoie False.

''')

def fct1(phrase):
    out_phrase = ""
    for c in phrase:
        out_phrase = c + out_phrase
    return out_phrase

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