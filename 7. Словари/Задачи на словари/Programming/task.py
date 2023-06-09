# Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык.
# Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу
# создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из
# этого словаря.
#
# Формат входных данных
#
# В первой строке задано одно целое число n — количество слов в словаре. В следующих n строках записаны слова и их
# определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число m — количество
# поисковых слов, чье определение нужно вывести. В следующих m строках записаны сами слова, по одному на строке.
#
# Формат выходных данных
#
# Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его
# определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.


num = int(input())
word_info = {}
words = tuple(tuple(i for i in input().split(": ")) for _ in range(num))
translate = []
for key, value in words:
    word_info[key.lower()] = value
for i in range(int(input())):
    translate.append(word_info.get(input().lower(), "Не найдено"))
print(*translate, sep="\n")
