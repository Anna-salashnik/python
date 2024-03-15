counter = 0
#Первый вопрос
answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Второй вопрос
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Пайтон":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно") 
#Третий вопрос
answer = input("Какой сегодня год?\n")
if answer == "2024" or answer == "две тысячи двадцать четвертый":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно") 
 #Четвертый вопрос
answer = input("Какая у нас специальность?\n")
if answer == "Programmer" or answer == "Программист":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно") 
#Вывод результата
print(f"вы набрали баллов {counter}")
