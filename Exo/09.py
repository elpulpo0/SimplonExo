# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres pairs de la liste initiale.

print("")
print (f'{"Exo n°09" :=^40}')
print("")

def findPairNumbers(listOfNumber):
    pairNumbers = list()
    for i in listOfNumber:
        if i % 2 == 0:
            pairNumbers.append(i)
        else:
            pass
    return pairNumbers

userListOfNumber = [2, 5, 6, 9, 15, 24]

pairsFromUserList = findPairNumbers(userListOfNumber)

print("Les nombres pair de la liste sont:", pairsFromUserList)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")