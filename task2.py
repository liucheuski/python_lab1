# 8	Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
import numpy

def getData():
    number = int(input("Попробуем еще разок\nВведите натуральное четырехзначное число: \n"))
    return number

def define(number, x):
    string = str(number)
    numbers = list(string)
    while x != len(numbers) - 1:

        for i in numpy.arange(0, len(numbers), 1):
            if numbers.count(numbers[i + x]) > 1:
                print("В вашем числе как минимум дважды повторяется цифра " + str(numbers[i + x]))
                main()
            else:
                define(number, x + 1)
                print("В вашем числе все " + str(number) + " цифры разные")
                main()

def main():
    number = getData()
    if number <= 0 or number > 9999:
        print("Вы нарушили условие задачи.  Число должно быть от 1 до 9999")
        main()
    else:
        print(str(define(number, 0)))
        main()

while True:
    main()
