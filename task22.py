from random import randint
n = int(input('Введите размер первого массива N = '))
m = int(input('Введите размер второго массива M = '))
lst1 = [randint(0, 10) for i in range(n)]
lst2 = [randint(0, 10) for i in range(m)]
set_lst1 = set (lst1)
print (lst1)
print(set_lst1)
print(lst2)
print(set (lst2))
for i in lst2:
    if i not in set_lst1 :
        lst1.append(i)
print(set (lst1))

