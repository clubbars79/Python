a = int(input('Введите число '))
b = int(input('Введите степень '))


def exponent(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * exponent(a, b - 1))


print(exponent(a, b))
