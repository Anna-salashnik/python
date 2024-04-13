massa = float(input("Введи массу конфет в граммах: "))
if massa > 2000:
    chena = massa / 1000 * 200
    print(f"200.0 руб за 1кг, Итого:{chena} руб")
else:
    chena = massa / 1000 * 250
    print(f"250.0 руб за 1кг, Итого:{chena} руб")
