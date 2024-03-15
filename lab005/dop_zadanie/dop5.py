import turtle

# Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()

# Рисуем крышу дома
t.penup()
t.goto(-50, -50)
t.pendown()
t.color("brown")
t.begin_fill() 
t.goto(-50, -50)
t.goto(0, 50)
t.goto(50, -50)
t.goto(-50, -50)
t.end_fill()

# Рисуем квадрат для дома
t.penup()
t.goto(-50, -50)
t.pendown()
t.color("black")
t.begin_fill()
for _ in range(4):  # количество линий
    t.forward(100)
    t.right(90)
t.end_fill()

# Рисуем дверь
t.penup()
t.color("blue")
t.goto(-20, -150)
t.pendown()
t.setheading(90)
t.begin_fill()
for _ in range(2):
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
t.end_fill()

# Рисуем окно
t.penup()
t.color("yellow")
t.goto( -30, -80)
t.pendown()
t.setheading(0)
t.begin_fill()
for _ in range(4):
    t.forward(20)
    t.right(90)
t.end_fill()
# Рисуем окно 2
t.penup()
t.color("yellow")
t.goto( 10, -80)
t.pendown()
t.setheading(0)
t.begin_fill()
for _ in range(4):
    t.forward(20)
    t.right(90)
t.end_fill()

# Скрыть черепашку и показать окно с нарисованным домом
t.hideturtle()
screen.mainloop()