import array

import numpy

# task1
# 12 Eсть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?
n = int(input("Введите число от 10 до 99 \n"))
print("Вы ввели: " + str(n))
string = str(n)
numbers = list(string)
if "1" in numbers or "9" in numbers:
    print("Ваше число содержит числа 1 или 9")
else:
    print("Ваше число не содержит чисел 1 или 9")
