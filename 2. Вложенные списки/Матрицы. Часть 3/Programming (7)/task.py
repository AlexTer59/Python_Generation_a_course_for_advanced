# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# заполнив её "змейкой" в соответствии с образцом.
#
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇


n, m = input().split()
n, m = int(n), int(m)
matrix = [[0 for j in range(m)] for i in range(n)]
counter = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            counter += 1
            matrix[i][j] = counter
    if i % 2 != 0:
        for j in range(len(matrix[i]) - 1, -1, -1):
            counter += 1
            matrix[i][j] = counter
    print("".join(str(x).ljust(3) for x in matrix[i]))
