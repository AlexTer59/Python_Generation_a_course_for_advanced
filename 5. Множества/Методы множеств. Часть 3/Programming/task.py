# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
#
# Формат входных данных
# На вход программе подаются два натуральных числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.


set1 = set(input())
set2 = set(input())
if not set1.isdisjoint(set2):
    print("YES")
else:
    print("NO")
