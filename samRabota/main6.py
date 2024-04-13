import turtle

# Получаем радиус первого круга от пользователя
radius = float(input("Введите радиус первого круга (синего): "))

# Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()

# Выбираем скорость рисования
t.speed(4)
# Рисуем синий круг без заливки (только контур)

# Рисуем остальные круги вокруг первого круга без заливки
colors = ["blue", "red", "green", "orange", "purple"]
for i in range(1, 6):
    t.penup()
    t.goto(0, -radius * (i + 1))
    t.pendown()
    t.pencolor(colors[i-1])
    t.circle(radius * (i + 1), None, 100)  # None используется для не заливки круга

# Закрываем черепашку по клику
screen.exitonclick()
