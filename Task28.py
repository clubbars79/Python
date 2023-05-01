a = int(input('Введите число А = '))
b = int(input('Введите степень В = '))


def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a


print(summa(a, b))
