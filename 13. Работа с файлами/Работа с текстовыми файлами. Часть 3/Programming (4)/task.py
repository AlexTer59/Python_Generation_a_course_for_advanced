# Однажды Жака Фреско спросили:
#
# "Если ты такой умный, почему не богатый?"
#
# Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
#
# "Были разноцветные козлы. Сколько?"
#
# "Сколько чего?"
#
# "Сколько из них составляет более 7% от общего количества козлов?"
#
# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех
# возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных
# цветов. Перечень козлов включает только строки из первого списка.
#
# Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки
# от Жака Фреско.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
#
# Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов,
# которые удовлетворяют условию загадки Жака Фреско.
#
# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
#
# Примечание 2. Если бы файл goats.txt содержал строки:
#
# COLOURS
# Pink goat
# Green goat
# Black goat
# GOATS
# Pink goat
# Pink goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Green goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# то файл answer.txt имел бы вид:
#
# Black goat
# Pink goat


with open('goats.txt', 'r', encoding='utf-8') as file1, open('answer.txt', 'w', encoding='utf-8') as file2:
    dict_of_goats = {}
    file1.readline()
    dict_of_goats = {i.rstrip(): 0 for i in file1.readlines() if i.rstrip() != 'GOATS'}
    dict_of_goats = sorted(dict_of_goats.items(), key=lambda x: x[0])
    dict_of_goats = dict(dict_of_goats)
    file1.seek(0)
    for _ in range(len(dict_of_goats) + 2):
        file1.readline()
    for line in file1.readlines():
        dict_of_goats[line.rstrip()] += 1
    for key, value in dict_of_goats.items():
        if value / sum(dict_of_goats.values()) >= 0.071:
            print(key, file=file2)
