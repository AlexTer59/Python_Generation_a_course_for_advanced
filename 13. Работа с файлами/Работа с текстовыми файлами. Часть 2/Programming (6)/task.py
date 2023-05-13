# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
#
# Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их,
# каждую на отдельной строке.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.
#
# Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:
#
# Aaron
# Abdul
# Abe
# Abel
# Abraham
# Albert
# и
#
# Abramson
# Adamson
# Adderiy
# Addington
# Adrian
# Albertson
# Einstein
# то результатом могло быть:
#
# Abdul Albertson
# Abel Adamson
# Albert Einstein


from random import sample

with open('first_names.txt', 'r', encoding='utf-8') as file1, open('last_names.txt', 'r', encoding='utf-8') as file2:
    full_names = zip(sample(file1.readlines(), 3), sample(file2.readlines(), 3))
    for first_name, last_name in full_names:
        print(first_name.rstrip(), last_name.rstrip())
