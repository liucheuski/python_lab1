# 11	Удалить пять первых нечетных по значению элементов списка.
import random
import numpy

odd = 0
list = []
result = []


def main():
    global odd
    length = int(input("Введите длиннy списка и мы заполним его случайными числами от 1 до 100\n"))
    for i in range(int(length)):
        element = random.randint(1, 100)
        list.append(element)
    print("У вас получился вот такой список: \n" + str(list))
    print("А теперь программа удалит пять первых нечетных по значению,\n"
          "конечно если их там не меньше пяти. В таком случае программа удалит их все  ")
    for i in numpy.arange(0, len(list), 1):
        if (list[i] % 2) != 0:
            odd = odd + 1
    print("В списке оказалось " + str(odd) + " нечентых чисел")
    list.sort()
    print("Отсортированный список " + str(list))
    if odd > 5:
        odd = 5


def do():
    for x in numpy.arange(0, len(list), 1):
        if (list[x] % 2) != 0:
            result.append(list[x])
    for x in numpy.arange(0, odd, 1):
        list.remove(result[x])
        print("Удалено: " + str(result[x]))
    print("Итоговый список " + str(list))

main()
do()
