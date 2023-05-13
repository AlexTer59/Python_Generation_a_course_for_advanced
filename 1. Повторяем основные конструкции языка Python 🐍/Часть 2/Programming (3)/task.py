# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
# Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
# а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
#
# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.
#
# Формат выходных данных
# Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы одним пробелом.


str = input().split(' ')
for i in range(len(str) - 1):
    str[i], str[len(str) - 1] = str[len(str) - 1], str[i]
print(*str, sep=' ')
