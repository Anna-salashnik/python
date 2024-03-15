import turtle
# Создали экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()
# Количество углов 
kolvo = int(input("Введите количество углов (3 для треугольника, 4 для квадрата, 5 для пятиугольника): "))

# Условие
if kolvo < 3 or kolvo > 5:
    print("Ошибка! Неправильное количество углов для фигуры.")
else:
    # Количество углов от 360 градусов
    angle = 360 / kolvo
    for _ in range(kolvo):
        t.forward(100)  
        # Длина 
        t.right(angle)
# Конец
screen.mainloop()
