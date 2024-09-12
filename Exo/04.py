# Écrivez une fonction qui prend un nombre entier en entrée et affiche si ce nombre est positif, négatif ou nul.

print("")
print (f'{"Exo n°04" :=^40}')
print("")

def isNumberPosOrNegOrNul(number):
    if number > 0:
        print(number, "is positive")
    elif number < 0:
        print(number, "is negative")
    elif number == 0:
        print(number, "is null")

numberToVerify = int(input("Ecris un nombre entier:"))
verifiedNumber = isNumberPosOrNegOrNul(numberToVerify)

print("")
print (f'{"Fin de l'exo" :=^40}')
print("")
