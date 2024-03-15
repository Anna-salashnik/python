import turtle

# Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()

# Запрашиваем у пользователя количество углов для фигур
num_sides = int(input("Введите количество углов (3 для треугольника, 4 для квадрата, 5 для пятиугольника): "))

# Проверяем, может ли черепаха нарисовать фигуру с таким количеством углов
if num_sides < 3 or num_sides > 5:
    print("Черепаха не может нарисовать фигуру с таким количеством углов.")
else:
    # Рисуем фигуру в зависимости от количества углов
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)  # Длина стороны
        t.right(angle)

# Завершаем рисование
screen.mainloop()
