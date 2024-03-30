import random

def get_user_choice():
    while True:
        answer = input("Что выберешь?\n").lower()
        options = {"к": "камень", "н": "ножницы", "б": "бумага", "я": "ящерица", "с": "спок"}
        for key, value in options.items():
            if value.startswith(answer):
                return key
        print("Выберите среди 'камень', 'ножницы', 'бумага', 'ящерица' или 'спок'.")

def determine_winner(player, bot):
    rules = {
        "к": ["н", "я", "б", "с"],
        "н": ["б", "я", "с", "к"],
        "б": ["к", "с", "н", "я"],
        "я": ["б", "к", "н", "с"],
        "с": ["н", "б", "я", "к"]
    }
    if player == bot:
        return "Ничья!"
    elif bot in rules[player]:
        return "Ты победил!"
    else:
        return "Я победил!"

print("Добро пожаловать в игру 'Камень, Ножницы, Бумага, Ящерица, Спок'!")
playerScore = 0
botScore = 0

for i in range(3):
    answer = get_user_choice()
    botAnswer = random.choice(list(rules.keys()))
    print(f"А я выберу {botAnswer}")

    result = determine_winner(answer, botAnswer)
    print(result)

    if "победил" in result:
        playerScore += 1
    elif "победил" in result:
        botScore += 1

if playerScore == botScore:
    print("Ничья по итогам трех раундов!")
elif playerScore > botScore:
    print("Ты победил по итогам трех раундов!")
else:
    print("Я победил по итогам трех раундов!")
