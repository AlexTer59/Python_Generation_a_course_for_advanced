# Напишите программу, которая возводит квадратную матрицу в m-ую степень.
#
# Формат входных данных На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы, затем натуральное число m.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
step = int(input())
res_matrix = [[0 for i in range(n)] for _ in range(n)]
temp_matrix = matrix
for _ in range(step - 1):
    res_matrix = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res_matrix[i][j] += temp_matrix[i][k] * matrix[k][j]
    temp_matrix = res_matrix
for i in range(n):
    print(*temp_matrix[i])
