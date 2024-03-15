import random
# Генерируем случайное число от 1 до 10
secret_number = random.randint(1, 10)

# Получаем ввод от пользователя
vvod = int(input("Угадайте секретное число от 1 до 10: "))

# Проверяем правильность угадывания и сообщаем "горячо-тепло-холодно"
if vvod == secret_number:
    print("Поздравляем! Вы угадали число.")
elif abs(vvod - secret_number) <= 2:
    print("Горячо! Вы близки к секретному числу.")
elif abs(vvod - secret_number) <= 4:
    print("Тепло! Вы неплохо угадываете.")
else:
    print("Холодно! Попробуйте еще раз.")

print(f"Секретное число было: {secret_number}")
