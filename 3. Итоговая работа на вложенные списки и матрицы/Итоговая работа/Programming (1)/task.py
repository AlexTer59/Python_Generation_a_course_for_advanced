# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
#
# 0 0 1
# 0 1 1  ----> (1 - заштрихованная область)
# 1 1 1
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы побочной диагонали также учитываются.


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = matrix[n - 1][n - 1]
for i in range(n):
    for j in range(n):
        if j >= n - i - 1:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
print(maximum)
