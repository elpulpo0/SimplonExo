# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres positifs.

def positiveNumberList(listToEdit):
    newList = [f for f in listToEdit if f > 0]
    return newList

# listToEdit = list((int(input("Ecris une liste de nombre:"))))
listToEdit = [4, -6, 7, -8]

editedList = positiveNumberList(listToEdit)

print(editedList)