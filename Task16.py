from random import randint
s=0
n = int(input('Введите размер массива N = '))
array = list()
for i in range (n):
    array.append (randint(0,10)) 
print (array) 
x = int(input('Введите число X '))
for i in range (n):
    if array[i] == x:
        s=s+1
print ('Количество чисел = ',x,' , ',s)