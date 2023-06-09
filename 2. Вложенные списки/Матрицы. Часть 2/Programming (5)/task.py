# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно
# горизонтальной оси симметрии.
#
# Формат входных данных На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range((n + 1) // 2):
    for j in range(n):
        matrix[i][j], matrix[n - 1 - i][j] = matrix[n- 1 - i][j], matrix[i][j]

for i in range(n):
    print(*matrix[i])



