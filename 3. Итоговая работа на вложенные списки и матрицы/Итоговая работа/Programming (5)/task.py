# Латинским квадратом порядка n называется квадратная матрица размером n×n, каждая строка и каждый столбец которой
# содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная квадратная матрица
# латинским квадратом.
#
# Формат входных данных На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.
#
# Формат выходных данных
# Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.


n = (int(input()))
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = True
for i in range(n):
    temp_list = [i for i in range(1, n + 1)]
    for j in range(n):
        if matrix[i][j] in temp_list:
            temp_list.remove(matrix[i][j])
        else:
            flag = False
            break
for i in range(n):
    temp_list = [i for i in range(1, n + 1)]
    for j in range(n):
        if matrix[j][i] in temp_list:
            temp_list.remove(matrix[j][i])
        else:
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")
