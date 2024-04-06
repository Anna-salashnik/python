import random

timeList = ["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]

while True:
    zodiac_sign = input("Введите знак Зодиака: ")
    
    # Проверяем корректность введенного знака Зодиака
    valid_signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
    if zodiac_sign.capitalize() not in valid_signs:
        print("Пожалуйста, введите корректный знак Зодиака.")
        continue
    
    time = timeList[random.randint(0, len(timeList) - 1)]
    event = eventList[random.randint(0, len(eventList) - 1)]
    object = objectList[random.randint(0, len(objectList) - 1)]
    
    print(time + " " + event + " " + object)
    
    next_try = input("Хотите попробовать ещё раз? (да/нет): ")
    if next_try.lower() != "да":
        break

print("Приходите ещё за новыми предсказаниями!")