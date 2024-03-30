import random

print("Добро пожаловать в игру 'Камень, Ножницы, Бумага, Ящерица, Спок'!")
playerScore = 0
botScore = 0

rules = {
    "к": ["н", "я", "б", "С"],
    "н": ["б", "я", "С", "к"],
    "б": ["к", "С", "н", "я"],
    "я": ["б", "к", "н", "С"],
    "С": ["н", "б", "я", "к"]
}

for i in range(3):
    answer = input("Что выберешь?\n").lower()
  
    if answer in {"камень", "камень", "к"}:
        answer = "к"
    elif answer in {"ножницы", "ножницы", "н"}:
        answer = "н"
    elif answer in {"бумагу", "бумага", "б"}:
        answer = "б"
    elif answer in {"ящерица", "ящерицу", "я"}:
        answer = "я"
    elif answer in {"с", "спок"}:
        answer = "С"
    else:
        print("Такого варианта нет, выберите среди 'камень', 'ножницы', 'бумага', 'ящерица' или 'Спок'")
        continue
  
    botAnswer = random.choice(list(rules.keys()))
    print(f"А я выберу {botAnswer}")

    if answer == botAnswer:
        print("Ничья!")
    elif botAnswer in rules[answer]:
        print("Ты победил!")
        playerScore += 1
    else:
        print("Я победил!")
        botScore += 1

if playerScore == botScore:
    print("Ничья по итогам трех раундов!")
elif playerScore > botScore:
    print("Ты победил по итогам трех раундов!")
else:
    print("Я победил по итогам трех раундов!")
