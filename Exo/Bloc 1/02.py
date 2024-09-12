# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres positifs.

print("")
print (f'{"Exo n°02" :=^40}')
print("")

def positiveNumberList(listToEdit):
    newList = [f for f in listToEdit if f > 0]
    return newList

# listToEdit = list((int(input("Ecris une liste de nombre:"))))
listToEdit = [4, -6, 7, -8]

editedList = positiveNumberList(listToEdit)

print(editedList)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")