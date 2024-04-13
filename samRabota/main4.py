import turtle

# Создаем черепашку
square = turtle.Turtle()
square.shape("turtle")

for i in range(180):  # Итерация от 0 до 179
    square.speed(10)  # Устанавливаем скорость черепашки
    square.forward(i)  # Рисуем отрезок длиной i
    square.left(91)  # Поворачиваем на 91 градус влево

# Ждем Enter для завершения
input("Нажмите клавишу Enter для продолжения: ")