# Écrivez un programme qui demande à l'utilisateur de saisir un mot et affiche si ce mot contient plus de 5 caractères.

def isWordContainMorethan5characters(word):
    # for carac in word:
    #     print(carac)
    # print(len(word))
    if len(word) > 5:
        print("Le mot", word, "contient plus de 5 caractères")
    else:
        print("Le mot", word, "contient moins de 5 caractères")

wordToCheck = input("Ecris un mot:")

wordChecked = isWordContainMorethan5characters(wordToCheck)

