
min_num = int(input('Введите минимальный элемент = '))
max_num = int(input('Введите максимальный элемент = '))
array = [1, 3,5,-6,8,-2,4,7,0,-6,2,5,7,2,-2,1,-1,-1,-1]
for i in range(len(array)):
    if min_num <= array[i] <= max_num:
        print (i)