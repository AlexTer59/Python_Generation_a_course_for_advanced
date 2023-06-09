# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю,
# левую и правую.
#
# Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой
# четверти.
#
# Формат входных данных На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Элементы диагоналей не учитываются.


num = int(input())
matrix = []
right, left, upper, lower = 0, 0, 0, 0

for i in range(num):
    matrix.append(list(map(int, input().split(' '))))

for i in range(num):
    for j in range(num):
        if j > i > (num - 1 - j):
            right += matrix[i][j]
        elif j < i < (num - 1 - j):
            left += matrix[i][j]
        elif i < j and i < (num - 1 - j):
            upper += matrix[i][j]
        elif i > j and i > (num - 1 - j):
            lower += matrix[i][j]
print("Верхняя четверть:", upper)
print("Правая четверть:", right)
print("Нижняя четверть:", lower)
print("Левая четверть:", left)
