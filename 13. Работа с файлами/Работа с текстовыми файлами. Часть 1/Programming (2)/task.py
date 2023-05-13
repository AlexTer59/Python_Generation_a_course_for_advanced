# Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную
# строку из этого файла.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести случайную строку указанного файла.
#
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
#
# Примечание 2. Гарантируется, что файл содержит хотя бы одну строку.
#
# Примечание 3. Не забудьте закрыть файл 🙂.


from random import randrange

file = open('lines.txt', 'r', encoding='UTF-8')
lines = []
for line in file:
    lines.append(line.rstrip())
print(lines[randrange(len(lines))])
file.close()
