# Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,
# n2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите
# программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
#
# Формат входных данных На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.
#
# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.


n = int(input())
check_list = [i for i in range(1, n * n + 1)]

flag = True

matrix = [[int(i) for i in input().split()] for _ in range(n)]

res = sum(matrix[0])
while flag:
    for i in range(n):
        if sum(matrix[i]) != res:
            flag = False
            break

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != res:
            flag = False
            break

    main_diag = 0
    sec_diag = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in check_list:
                check_list.remove(matrix[i][j])
            else:
                flag = False
                break
            if i == j:
                main_diag += matrix[i][j]
            if j == n - 1 - i:
                sec_diag += matrix[i][j]
    if len(check_list) != 0:
        flag = False
        break
    if main_diag != res or sec_diag != res:
        flag = False
        break
    break
if flag:
    print("YES")
else:
    print("NO")
