# На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
#
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел
# одинаковая сумма цифр, их следует вывести в порядке неубывания.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#
# Формат выходных данных
# Программа должна вывести отсортированный список чисел в соответствии с условием задачи,
# разделяя его элементы одним пробелом.


def comporator(x):
    return sum([int(x) for x in str(x)]), x


numbers = [int(i) for i in input().split()]

print(*sorted(numbers, key=comporator))
