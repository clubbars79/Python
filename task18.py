#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
from random import randint
n = int(input('Введите размер массива N = '))
array = list()
arr = list()
for i in range (n):
    array.append (randint(0,100)) 
    arr.append (randint(0,0))
print (array) 
x = int(input('Введите число X '))
for i in range (n):
    arr[i] = abs(array[i]-x)     
s=arr.index(min(arr))
print ('Близкое по значению число = ' ,array[s])