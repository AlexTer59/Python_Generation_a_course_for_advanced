# На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение выражения:
# e^d+ln(d)+lg(d)+√d
#
# Формат входных данных
# На вход программе подается положительное десятичное число d.
#
# Формат выходных данных
# Программа должна вывести искомое значение выражения.


import decimal

d = decimal.Decimal(input())
print(decimal.Decimal.exp(d) + decimal.Decimal.ln(d) + decimal.Decimal.log10(d) + decimal.Decimal.sqrt(d))
