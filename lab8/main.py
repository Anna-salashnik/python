import random

print("Добро пожаловать в игру камень, ножницы, бумага, ящерица, спок!")

playerScore = 0
botScore = 0

for i in range(3):
    answer = input("Что выберешь?\n").lower()
    
    if answer.find("камень") != -1:
        answer = "к"
    elif answer.find("ножницы") != -1:
        answer = "н"
    elif answer.find("бумага") != -1 or answer.find("бумагу") != -1:
        answer = "б"
    elif answer.find("ящерица") != -1:
        answer = "я"
    elif answer.find("спок") != -1:
        answer = "с"
    
    botAnswer = random.choice(["камень", "ножницы", "бумагу", "ящерица", "спок"])
    print(f"А я выберу {botAnswer}")
    
    botAnswer = botAnswer[0]
    
    print(botAnswer)
    
    if answer == botAnswer:
        print("Ничья!")
    elif (answer == "к" and (botAnswer == "н" or botAnswer == "я")) or \
         (answer == "н" and (botAnswer == "б" or botAnswer == "я")) or \
         (answer == "б" and (botAnswer == "к" or botAnswer == "с")) or \
         (answer == "я" and (botAnswer == "б" or botAnswer == "к")) or \
         (answer == "с" and (botAnswer == "н" or botAnswer == "я")):
        print("Ты победил!")
        playerScore += 1
    else:
        print("Я победил!")
        botScore += 1

if playerScore == botScore:
    print("Ничья по итогам трёх раундов!")
elif playerScore > botScore:
    print("Ты победил по итогам трёх раундов")
else: 
    print("Я победил по итогам трёх раундов")
