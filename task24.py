from random import randint
n = int(input('Введите количество кустов N = '))
lst1 = [randint(0, 50) for i in range(n)]
lst2 = [int(i) for i in range(n)]
#set_lst1 = set (lst1)
print (lst2)
print(lst1)
slov = (dict(zip(lst2,lst1)))
s = [value for key, value in slov.items() if key < 3 ]
print(s)
#print(set (lst2))
#for i in lst2:
#    lst1.append(i)
#print(set (lst1))
