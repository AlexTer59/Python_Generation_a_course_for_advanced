# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m и
# заполняет её числами от 1 до n⋅m в соответствии с образцом.
#
# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
#
# Формат выходных данных
# Программа должна вывести матрицу в соответствии с образцом.
#
# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого
# используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇


n, m = input().split()
n, m = int(n), int(m)
matrix = [[int(i + j * m) for i in range(1, m + 1)] for j in range(n)]
for i in range(n):
    print(''.join(str(x).ljust(3) for x in matrix[i]))
