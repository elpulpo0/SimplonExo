exo = 37
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle liste contenant 
les mots dont la première lettre est une voyelle (a, e, i, o, u) en utilisant une boucle "while".

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



# Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle 
# liste contenant les mots dont la première lettre est une voyelle (a, e, i, o, u).

print("")
print (f'{"Exo n°03" :=^40}')
print("")

def startWithVoyelleList(listToEdit):
    voyelles = ("a", "e", "i", "o", "u")
    newList = [f for f in listToEdit if f.startswith(voyelles)]
    return newList

listToEdit = ["abricot", "banane", "orange", "pomme"]

editedList = startWithVoyelleList(listToEdit)

print(editedList)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")