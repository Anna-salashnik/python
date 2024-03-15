levels = 5  # Уровни елочки
for i in range(1, levels+1):
    stars = '*' * (2*i - 1)
    print(stars.center(2*levels + 1))