# Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с
# ним решать задачи по программированию.
#
# Формат входных данных
#
# На вход программе в первой строке подается число n – общее количество учеников. Далее идут n строк, содержащих
# имена и фамилии учеников.
#
# Формат выходных данных
#
# Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного
# друга, разделённые дефисом.
#
# Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть тайным другом для
# нескольких учеников.
#
# Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны и другие способы выбора тайных
# друзей.


import random

pair = {}
students = []
students = [input() for i in range(int(input()))]
students_friend = students.copy()
random.shuffle(students_friend)

for i in range(len(students)):
    while students[i] == students_friend[i]:
        if len(students_friend) - i == 1:
            students_friend[i], students_friend[i - 1] = students_friend[i - 1], students_friend[i]
        else:
            random.shuffle(students_friend)
for i in range(len(students)):
    print(students[i], '-', students_friend[i])
