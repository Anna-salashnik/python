from turtle import *
from random import randint

shape("turtle")

colors = ["blue", "red", "orange", "purple"]
shredder = randint(1, 10)

user_choose = 0
while user_choose != shredder:
    user_choose = str.lower(input("Выберите направление Left/Right/Direct/Back: "))

    if user_choose == "left":
        left(90)
        for color_turtle in colors:
            pensize(randint(1, 10))
            color(color_turtle)
            forward(randint(5, 30))
    
    elif user_choose == "right":
        right(90)
        for color_turtle in colors:
            pensize(randint(1, 10))
            color(color_turtle)
            forward(randint(5, 30))
    
    elif user_choose == "direct":
        for color_turtle in colors:
            pensize(randint(1, 10))
            color(color_turtle)
            forward(randint(5, 30))
    
    elif user_choose == "back":
        left(180)
        for color_turtle in colors:
            pensize(randint(1, 10))
            color(color_turtle)
            forward(randint(5, 30))
    
    user_choose = randint(1, 10)
    
    if user_choose != shredder:
        print("Шреддер не здесь, продолжаем поиски")
    else:
        print("Шреддер найден!")

