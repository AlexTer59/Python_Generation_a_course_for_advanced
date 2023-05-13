# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, состоящих из строчных и
# прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
#
# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной
# букве в верхнем и нижнем регистре.
#
# Формат входных данных
# На вход программе подаются два числа n и m, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести n паролей длиной m символов в соответствии с условием задачи, каждый на отдельной строке.
#
# Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать возможно.
#
# Примечание 2. Решение задачи удобно оформить в виде двух вспомогательных функций:
#
# функция generate_password(length) – возвращает случайный пароль длиной length символов; функция generate_passwords(
# count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.


import string
import random


def generate_passwords(count, length):
    symbols = [x for x in (string.ascii_letters + string.digits) if x not in ('lI1oO0')]
    #
    numbers = [x for x in (string.digits) if x not in ('lI1oO0')]
    lower_letters = [x for x in (string.ascii_lowercase) if x not in ('lI1oO0')]
    upper_letters = [x for x in (string.ascii_uppercase) if x not in ('lI1oO0')]
    return [''.join(
        random.sample(symbols, length - 3) + random.sample(upper_letters, 1) + random.sample(lower_letters, 1) + (
            random.sample(numbers, 1))) for _ in range(count)]


n, m = int(input()), int(input())
passwords = generate_passwords(n, m)
for i in passwords:
    print(*random.sample(i, m), sep='')
