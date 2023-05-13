# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в
# порядке возрастания, которые есть как в первой строке, так и во второй.
#
# Формат входных данных
# На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести множество чисел, встречающихся в обеих строках.


set1 = set(input().split())
set2 = set(input().split())
res = set1 & set2
print(*sorted([int(i) for i in res]))
