import turtle
# Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()
# Выбираем количество концов звезды (5-9)
num_p = 7
for _ in range(num_p):
    t.forward(100)  # Длина луча
    t.right(360 / num_p * 2)  # Угол поворота для создания звезды
# Завершаем рисование
screen.mainloop()

