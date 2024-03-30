studentList = ["Вася", "Петя", "Андрей", "Руслан", "Роман"]
gradeList = [4, 3, 5, 4, 5]

while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента\n"
                       "2-удалить студента по имени\n"
                       "3-посмотреть весь список студентов\n"
                       "4-добавить оценку студенту\n"
                       "5-удалить студента по номеру\n"
                       "6-посмотреть список оценок\n"
                       "0-выйти из программы\n"))

    if answer not in [1, 2, 3, 4, 5, 6, 0]:
        print("такой команды нет")
        continue

    elif answer == 1:
        newStudent = input("введите имя студента: ")
        studentList.append(newStudent)
        grade = int(input("введите оценку студента (от 1 до 5): "))
        gradeList.append(grade)

    elif answer == 2:
        delStudent = input("введите студента для удаления: ")
        if delStudent in studentList:
            index = studentList.index(delStudent)
            studentList.remove(delStudent)
            del gradeList[index]
            print("Удален")
        else:
            print("Такого студента нет в списке")

    elif answer == 3:
        print("Список студентов:", studentList)

    elif answer == 4:
        student = input("Введите имя студента, которому добавить оценку: ")
        if student in studentList:
            index = studentList.index(student)
            grade = int(input("Введите оценку для студента (от 1 до 5): "))
            gradeList[index] = grade
        else:
            print("Такого студента нет в списке")

    elif answer == 5:
        delNumber = int(input("введите номер студента для удаления: "))
        if delNumber < len(studentList):
            del studentList[delNumber]
            del gradeList[delNumber]
        else:
            print("Неверный номер студента")

    elif answer == 6:
        print("Список оценок:", gradeList)

    elif answer == 0:
        break
