# task 2
# 4. Фирма ежегодно на протяжении n лет закупала оборудование стоимостью соответственно s1, s2, ..., sn pублей в год
# (эти числа вводятся и обрабатываются последовательно). Ежегодно в результате износа и морального старения (амортизации)
# все имеющееся оборудование уценивается на р%. Какова общая стоимость накопленного оборудования за n лет?

from unicodedata import decimal

result = 0
data = dict()
data = {"1": 100, "2": 100}
choise = ""
percent = 10


def main(choise):
    match choise:
        case "1":
            addData()
        case "2":
            addPercent()
        case "3":
            getResult()
        case "4":
            recount()
        case "5":
            print("До свидания!")
            exit()


def addData():
    print("Введите год:")
    year = int(input())
    print("Введите стоимость оборудования за " + str(year) + " год:")
    sum = int(input())
    data.update({year: sum})


def addPercent():
    global percent
    percent = int(input("Введите процент аммортизации: "))


def getResult():
    years = []
    global choise
    global percent
    global result
    if len(data) == 0:
        choise = str(input("Вы ввели не достаточно данных для рачета, выберите п.1 меню"))
        main(choise)
    elif percent == 0:
        choise = str(input("Вы не ввели процент аммортизации, выберите п.2 меню"))
        main(choise)
    else:
        years = sorted(data.keys())
        firstYear = str(years[0])
        lastYear = str(years[len(years) - 1])
        for year in years:
            result = (result + data.get(year)) * (1 - percent / 100)
    print("Стоимость оборудование накопленного c " + str(firstYear) + " года по " + str(lastYear) + " год составляет:\n" +
          str(result) + " денег")


def recount():
    global percent
    global choise
    percent = 0
    data.clear()
    print("Введите данные для нового расчета. Предыдущие данные удалены")
    choise = str(input("Выберите пункт меню для продолжения работы: "))
    main(choise)


while choise != "5":
    choise = str(input(
        "Выберите пункт меню:\n 1. Ввести данные\n 2. Ввести % аммортизации\n 3. Закончить ввод и получить результат\n"
        " 4. Произвести новый расчет\n 5. Завершить программу"))
    main(choise)
