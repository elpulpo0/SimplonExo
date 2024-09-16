# Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle liste contenant la longueur de chaque mot.

print("")
print (f'{"Exo n°08" :=^40}')
print("")

def lenghtOfWords(listOfWords):
    listOfLenghts = list()
    for i in listOfWords:
        listOfLenghts.append(len(i))
    return listOfLenghts

print('La liste de mots est ["ceci", "est", "une", "liste", "de", "mots"]')
print("")

UserListOfWords = ["ceci", "est", "une", "liste", "de", "mots"]

answerList = lenghtOfWords(UserListOfWords)

print("Voici une liste représentant la longueur de chaque mot:", answerList)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")
