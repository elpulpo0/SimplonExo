# Écrivez un programme qui demande à l'utilisateur de saisir 5 nombres entiers, acquisition clavier, les stocke dans une liste, puis affiche la liste.

def numberList(numbers):
    newList = list(numbers)
    return newList

listToshow = list()

listToshow.append((input("Ecris un nombre entier:")))
listToshow.append((input("Ecris un deuxième nombre entier:")))
listToshow.append((input("Ecris un troisième nombre entier:")))
listToshow.append((input("Ecris un quatrième nombre entier:")))
listToshow.append((input("Ecris un cinquième nombre entier:")))

userList = numberList(listToshow)

print("Voici la liste des tes nombres", userList)
print("Longueur de la liste:", len(userList))

# Écrivez une fonction qui prend une liste de nombres en entrée et renvoie la somme de tous les éléments de la liste.

def sommeNumbersFromList(listOfNumbers):
    total = listOfNumbers[0] + listOfNumbers[1]
    return total

sommeUserList = sommeNumbersFromList(userList)
print("La somme des nombres de ta liste est:", sommeUserList)
    
