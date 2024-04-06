import turtle

turtle.shape("turtle")
turtle.speed(6)
colors = ["blue", "green", "pink", "red", "black"]  # Список цветов для смены

for i in range(5):
    turtle.color(colors[i % len(colors)])  # Меняем цвет на каждом кругу
    turtle.circle((i + 1) * 10)

turtle.done()
