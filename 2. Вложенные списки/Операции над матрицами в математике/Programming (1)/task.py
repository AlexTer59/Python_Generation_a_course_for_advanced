# Напишите программу, которая перемножает две матрицы.
#
# Формат входных данных На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой
# матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и
# столбцов второй матрицы затем элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.


n, m = input().split()
n, m = int(n), int(m)
matrix = [[int(m) for m in input().split()] for n in range(n)]
input()
n1, k = input().split()
n1, k = int(n1), int(k)
matrix2 = [[int(k) for k in input().split()] for n1 in range(n1)]

res_matrix = [[0 for k in range(k)] for n in range(n)]

for t_n in range(n):
    for t_k in range(k):
        for t_n1 in range(n1):
            res_matrix[t_n][t_k] += matrix[t_n][t_n1] * matrix2[t_n1][t_k]

    print(*res_matrix[t_n])
