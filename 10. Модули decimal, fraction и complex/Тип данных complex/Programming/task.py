# Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их сумму, разность и произведение.
#
# Формат входных данных
# На вход программе подается два комплексных числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести ответ на задачу


a = complex(input())
b = complex(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
