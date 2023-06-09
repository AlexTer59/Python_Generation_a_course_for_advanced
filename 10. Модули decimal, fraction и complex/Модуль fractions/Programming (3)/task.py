# Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и
# частное.
#
# Формат входных данных
# На вход программе подаются две ненулевые дроби, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сумму, разность, произведение и частное двух дробей.
#
# Примечание. Обратите внимание на третий тест: исходные дроби сокращать не нужно, а результат нужно.


from fractions import Fraction

n, m = input(), input()
print(n, '+', m, '=', Fraction(n) + Fraction(m))
print(n, '-', m, '=', Fraction(n) - Fraction(m))
print(n, '*', m, '=', Fraction(n) * Fraction(m))
print(n, '/', m, '=', Fraction(n) / Fraction(m))
