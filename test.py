# from numpy.random import rand
# tot = 1
# while tot>.5:
    
#     tot = rand()
#     print(tot)

a = input("écris:")
# print(a)
# print(type(a))
# print(len(a))

# for indice in range(len(a)):
#    print(a[indice])

#for carac in a:
#     print(carac)

list_num = list()
list_noNum = []

for carac in a:
    if carac.isnumeric():
        list_num.append(int(carac))
    else:
        list_noNum.append(carac)

print("")
print (f'{"Numeric" :=^40}')
print(list_num)
print("")
print (f'{"No Numeric" :=^40}')
print(list_noNum)
print("")