# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# заполнив её "спиралью" в соответствии с образцом.
#
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести матрицу в соответствии образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇


n, m = input().split()
n, m = int(n), int(m)
matrix = [[0 for j in range(m)] for i in range(n)]
counter = 0
step = 0

if m == 1:
    for i in range(0 + step, n - step):
        counter += 1
        matrix[i][m - 1 - step] = counter
if n == 1:
    for j in range(0 + step, m - step):
        counter += 1
        matrix[0 + step][j] = counter

while counter != n * m:
    for j in range(0 + step, m - step):
        counter += 1
        matrix[0 + step][j] = counter
    for i in range(1 + step, n - step):
        counter += 1
        matrix[i][m - 1 - step] = counter
    for j in range(m - 2 - step, -1 + step, -1):  # m - 2
        counter += 1
        matrix[n - 1 - step][j] = counter
    for i in range(n - 2 - step, 0 + step, -1):
        counter += 1
        matrix[i][0 + step] = counter
    step += 1

for i in range(n):
    print("".join(str(x).ljust(3) for x in matrix[i]))
