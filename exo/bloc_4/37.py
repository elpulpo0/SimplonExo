exo = 37
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend un nombre entier en entrée et affiche tous les 
nombres de 1 jusqu'à ce nombre (inclut) en utilisant une boucle "while".

''')


def fct(num):
    i = 1
    print("Voici la liste des nombre avant le tiens en partant de zéro:")
    while i <= num:
        print(i)
        i = i + 1

numUser = int(input("Ecris un nombre:"))

fct(numUser)

print(f'''

{"Fin de l'exo" :=^40}
''')