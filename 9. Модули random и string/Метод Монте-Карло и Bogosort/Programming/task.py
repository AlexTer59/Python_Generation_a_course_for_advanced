# Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы
# неравенств:
#
# −2 ≤x ≤2
# −2 ≤ y ≤ 2
# x^3 + y^4 + 2 ≥ 0
# 3*x + y^2 ≤ 2


import random

n = 10 ** 6  # количество испытаний
s0 = 16
k = 0
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
        k += 1

print((k / n) * s0)
