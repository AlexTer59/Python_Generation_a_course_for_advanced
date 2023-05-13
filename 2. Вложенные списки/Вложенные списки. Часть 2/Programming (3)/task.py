# На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника
# Паскаля.
#
# Формат входных данных
# На вход программе подается число n(n≥1).
#
# Формат выходных данных
# Программа должна вывести первые n строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.


num = int(input())


def pascal(num):
    list = []
    for i in range(1, num + 2):
        list.append([1 for i in range(1, i + 1)])

    if num > 1:
        for i in range(2, num + 1):
            for j in range(1, i):
                list[i][j] = list[i - 1][j - 1] + list[i - 1][j]

    return list[num]


for i in range(num):
    print(*pascal(i))
