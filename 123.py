ftext = input ("Введите имя файла для чтения ")
s = open (ftext) # открывает файл
name = (s.read()) # читает файл в переменную
repname = name.replace(" ","") # удаляем пробелы
print("Количество символов в файле = ", len(repname)) # считает количество символов
letter = input ("Какую букву будем считать? ")
b = repname.count(letter)
regname = repname.swapcase () #меняет регистр букв текста
c = regname.count (letter)
# c = swapcase (repname.count(letter))
if letter == "!" or "." or "," or "(":
    f = b
f = b + c
print("Количество букв ", letter, "=", f) #считает количество определенного символа
import time
time.sleep(15)