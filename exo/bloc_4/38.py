exo = 38
exo_title = f"Exo n°{exo}"

print(f'''
{exo_title :=^40}

Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle
 liste contenant uniquement les nombres positifs en utilisant une boucle "while".

''')

def fct(num_list):
    n = 0
    new_list = []
    while n < len(num_list):
        if num_list[n] > 0:
            new_list.append(num_list[n])
        n = n + 1
    return new_list
        

list_num = [6, 78, 54, 99, 56, 87, -87, -98]


print(f'''

{fct(list_num)}

{"Fin de l'exo" :=^40}
''')