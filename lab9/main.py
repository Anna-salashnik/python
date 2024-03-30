studentList = ["Вася", "Петя", "Андрей", "Руслан", "Роман"]
while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента\n"
                       "2-удалить студента по имени\n"
                       "4-удалить студента по номеру\n"
                       "3-посмотреть весь список студентов\n"
                       "0-выйти из программы\n"))

    if answer not in [1, 2, 3, 4, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента: ")
        studentList.append(newStudent)
     

    elif answer == 2:
        delStudent = input("введите студента для удаления: ")
        if delStudent in studentList:
            studentList.remove(delStudent)
            print(f"Удален студент '{delStudent}' ")
        else:
            print("Такого студента нет в списке")
    elif answer == 3:
        print(studentList)

    elif answer == 4:
        delNumber = int(input("введите номер студента для удаления"))
        studentList.pop(delNumber)
    elif answer == 0:
        break
