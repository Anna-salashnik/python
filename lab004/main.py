age = int(input("введите возраст"))
if age > 0 and age <= 10:
 print("вы ребёнок")
elif age > 10 and age <= 15:
 print("вы подросток")
elif age > 15 and age <= 25:
 print("вы юноша/девушка")
elif age > 25 and age <= 40:
 print("вы в полном рассвете сил")
elif age > 40 and age <= 50:
 print("вы опытный")
elif age > 50 and age <= 65:
 print("вы пожилой человек")
else:
 print("возраст введён не верно!")