# Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input ('Введите трехзначное число '))
if (999 > number and number > 100): 
    sum = int (number/100+number/10%10+number%10)
    print (sum)
else:
    print ('Вы ввели не трехзначное число')