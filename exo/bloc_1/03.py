# Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle liste contenant les mots dont la première lettre est une voyelle (a, e, i, o, u).

print("")
print (f'{"Exo n°03" :=^40}')
print("")

def startWithVoyelleList(listToEdit):
    voyelles = ("a", "e", "i", "o", "u")
    newList = [f for f in listToEdit if f.startswith(voyelles) ]
    return newList

listToEdit = ["abricot", "banane", "orange", "pomme"]

editedList = startWithVoyelleList(listToEdit)

print(editedList)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")