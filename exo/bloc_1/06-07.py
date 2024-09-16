# Écrivez un programme qui demande à l'utilisateur de saisir 5 nombres entiers, acquisition clavier, les stocke dans une liste, puis affiche la liste.

print("")
print (f'{"Exo n°06 et 07" :=^40}')
print("")

def numberList(numbers):
    newList = list()
    for i in numbers:
        newList.append(int(i))
    return newList

# userListOfNumbers = list()

# userListOfNumbers.append(int(input("Ecris un nombre entier:")))
# userListOfNumbers.append(int(input("Ecris un deuxième nombre entier:")))
# userListOfNumbers.append(int(input("Ecris un troisième nombre entier:")))
# userListOfNumbers.append(int(input("Ecris un quatrième nombre entier:")))
# userListOfNumbers.append(int(input("Ecris un cinquième nombre entier:")))

userListOfNumbers = (input("Ecris une liste de nombres entiers:")).split()

userList = numberList(userListOfNumbers)

print("Voici la liste des tes nombres", userList)
print("Longueur de la liste:", len(userList))

# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie la somme de tous les éléments de la liste.

def sumNumbersFromList(listOfNumbers):
    sum = 0
    for i in listOfNumbers:
        sum = sum + i
    return sum

sumUserList = sumNumbersFromList(userList)
print("La somme des nombres de ta liste est:", sumUserList)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")
    
