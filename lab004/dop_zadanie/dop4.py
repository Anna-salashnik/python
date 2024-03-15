amount = float(input("Введите сумму в рублях: "))
valuta = input("Выберите валюту для конвертации (USD - доллары, EUR - евро, CNY - юани): ")
usd = 91.87
eur = 99.97
cny = 12.73
if valuta == "USD":
    converted_amount = amount / usd
    print("Сумма в USD:", converted_amount)
elif valuta == "EUR":
    converted_amount = amount / eur
    print("Сумма в EUR:", converted_amount)
elif valuta == "CNY":
    converted_amount = amount / cny
    print("Сумма в CNY:", converted_amount)
else:
    print("Выбрана недопустимая валюта. Пожалуйста, выберите USD, EUR или CNY.")

