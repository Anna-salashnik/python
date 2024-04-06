import random 
# Заготовленные ответы для каждого из трех вопросов 
answers = [ 
    ["Подумай еще", "Хорошо", "Я не пойду"],    
    ["Красивая", "Ты не помнишь", "Естественно"], 
    ["Может повезет", "Здорово, отлично", "Я приглашаю"]  
    ] 
# Функция для голосового помощника 
def voice_assistant(): 
    for i in range(3): 
        question = input("Задайте вопрос: ") 
        if i == 0: 
            answer = random.choice(answers[0]) 
        elif i == 1: 
            answer = random.choice(answers[1]) 
        else: 
            answer = random.choice(answers[2]) 
             
        print("Ответ:", answer) 
 
voice_assistant()