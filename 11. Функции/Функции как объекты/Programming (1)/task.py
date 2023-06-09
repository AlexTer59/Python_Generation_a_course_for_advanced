# Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от
# начала координат (точки (0;0)). Программа должна вывести отсортированный список.
#
# Примечание. Расстояние от начала координат O(0;0) до точки A(x;y) равно OA=x2+y2−−−−−−√.
#
#
# Примечание. Используйте необязательный аргумент key.


points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]


def comporator(points):
    return (points[0] ** 2 + points[1] ** 2) ** 0.5


print(sorted(points, key=comporator))
