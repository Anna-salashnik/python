summa = float(input("Введи сумму: "))
valuta = input("Выбери - доллары, евро или юани: ")
dollar = 91.87
evro = 99.97
yani = 12.73

if valuta == "доллары":
    perevod = summa / dollar
    print("Сумма в долларах:", perevod)
elif valuta == "евро":
    perevod = summa / evro
    print("Сумма в евро:", perevod)
elif valuta == "юани":
    perevod = summa / yani
    print("Сумма в юанях:", perevod)
else:
    print("Ошибка! Выбери доллары, евро или юани.")

