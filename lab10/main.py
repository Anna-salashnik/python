rightCounter = 0
questionsCounter = 0
questions = ["Сколько цветов у радуги?", "Какой язык мы изучаем?", "Сколько дней в году?", "Кто такой Путин?"]
rightAnswers = ["7", "Python", "365", "Президент"]
while questionsCounter < len(questions):
    answer = input(questions[questionsCounter])
    if answer.lower() == rightAnswers[questionsCounter].lower():
        print("Вы ответили верно!")
        rightCounter += 1
    else:
        print("Вы ответили неверно.")
    questionsCounter += 1

print(f"Вы набрали баллов: {rightCounter}")