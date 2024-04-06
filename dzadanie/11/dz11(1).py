from turtle import *

# Запрашиваем у пользователя длину стороны квадрата
side_length = int(input("Введите длину стороны квадрата: "))

# Перемещаем черепашку в начальную точку для рисования квадрата
penup()
goto(-side_length/2, side_length/2)
pendown()

# Начинаем рисование квадрата
for _ in range(4):
    forward(side_length)
    right(90)

done()