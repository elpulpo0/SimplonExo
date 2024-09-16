exo = 36
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez un programme qui demande à l'utilisateur de deviner un nombre secret (par exemple 42). 
Le programme indique à l'utilisateur si le nombre à deviner est plus grand ou plus petit que sa 
proposition et continue de demander un nombre tant que l'utilisateur ne trouve pas le nombre secret. 
Une fois que l'utilisateur trouve le nombre secret, affichez un message de félicitations.

''')

secretCode = "666"

def fct(code):
    if code < secretCode:
        phraseUser = fct(input("Try again, it's bigger than that:"))
    elif code > secretCode:
        phraseUser = fct(input("Try again, it's smaller than that:"))
    else:
        print("""
Congrats, you found the code !!
        """)

phraseUser = input("Find the secret code:")

fct(phraseUser)

print(f'''

{"Fin de l'exo" :=^40}
''')