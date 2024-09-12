# Écrivez un programme qui prend une liste de mots en entrée, acquisition clavier, les trie par ordre alphabétique et affiche la liste triée.

print("")
print (f'{"Exo n°10" :=^40}')
print("")

def sortListOfWords(listOfWords):
    sortedList = sorted(listOfWords)
    return sortedList

# userListOfWords = ["une", "liste", "de", "mots"]
userListOfWords = input("Ecris une liste de mots:").split()

sortedUserList = sortListOfWords(userListOfWords)

print("Voici la liste triée par ordre alphabétique:", sortedUserList)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")