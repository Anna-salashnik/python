massa = float(input("Введи массу конфет в граммах: "))
if massa > 2000:
    chena = massa / 1000 * 200
else:
    chena = massa / 1000 * 250
print(f"Цена конфет: {chena} руб")