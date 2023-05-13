# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной
# строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Ведущие нули в числах должны игнорироваться.


num = set()
number = input().split()
for i in number:
    if int(i) not in num:
        num.add(int(i))
        print('NO')
    else:
        print('YES')
