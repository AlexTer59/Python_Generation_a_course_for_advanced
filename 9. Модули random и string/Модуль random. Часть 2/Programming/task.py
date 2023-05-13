# IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.
#
# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP
# адрес.


import random


def generate_ip():
    return '{}.{}.{}.{}'.format(*[random.randrange(256) for _ in range(4)])


print(generate_ip())
