# 16	Найти номера минимального и максимального элементов первой половины списка.
import random
import numpy


def generateList():
    list = []
    length = int(input("Введите длиннy списка и мы заполним его случайными числами от 1 до 100\n"))
    for i in range(length):
        element = random.randint(1, 100)
        list.append(element)
    print("У вас получился вот такой список: \n" + str(list))
    return list


def doIt(list):
    newList = []
    pivot = len(list) // 2
    min = list[0]
    max = list[0]
    minIndex = 0
    maxIndex = 0
    for i in numpy.arange(0, pivot, 1):
        newList.append(list[i])
        if list[i] < min:
            min = list[i]
            minIndex = i
        elif list[i] >= max:
            max = list[i]
            maxIndex = i
    print("Его перва половина выглядит вот так " + str(newList))
    return [minIndex, min, maxIndex, max]


while True:
    result = doIt(generateList())
    print(
        "Ваше минимально число = " + str(result[1]) + " и его позиция в списке " + str(
            result[0]+1) + "\n, а максимальное число = " + str(result[3]) + " и его позиция в списке " + str(result[2]+1))
