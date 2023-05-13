# Напишите программу, которая меняет местами столбцы в матрице.
#
# Формат входных данных На вход программе на разных строках подаются два натуральных числа n и m — количество строк и
# столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих
# обмену.
#
# Формат выходных данных
# Программа должна вывести указанную таблицу с замененными столбцами.


n, m = int(input()), int(input())
matrix = []
swap = []

for i in range(n):
    matrix.append(list(map(int, input().split(' '))))

swap.append(list(map(int, input().split(' '))))

for i in range(n):
    matrix[i][swap[0][0]], matrix[i][swap[0][1]] = matrix[i][swap[0][1]], matrix[i][swap[0][0]]

for i in range(n):
    print(*matrix[i], end=' ')
    print()
