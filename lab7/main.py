import random
# Генерирация случ числа от 1 до 10
chislo = random.randint(1, 10)
# Введи число
otvet = int(input("Угадай число от 1 до 10: "))
# Условие
if otvet == chislo:
    print("Ты угадал!")
elif abs(otvet - chislo) <= 2:
    print("Горячо!")
elif abs(otvet - chislo) <= 3:
    print("Тепло.")
else:
    print("Холодно.")

print(f"Сгенерированное число: {chislo}")
