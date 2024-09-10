# Écrivez une fonction qui prend un nombre entier en entrée et affiche si ce nombre est positif, négatif ou nul.

def isNumberPosOrNegOrNul(number):
    if number > 0:
        print(number, "is positive")
    elif number < 0:
        print(number, "is negative")
    elif number == 0:
        print(number, "is null")

numberToVerify = int(input("Ecris un nombre entier:"))
verifiedNumber = isNumberPosOrNegOrNul(numberToVerify)
