# На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
# которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
# отметьте символами *, остальные клетки заполните точками.
#
# Формат входных данных На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в
# виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 1
# до 8, снизу вверх)).
#
# Формат выходных данных
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.


column = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

matrix = [['.' for _ in range(8)] for _ in range(8)]

pos = list(input())
pos[0], pos[1] = (8 - (int(pos[1]))), (column[pos[0]])
matrix[pos[0]][pos[1]] = 'N'

for i in range(-2, 3):
    if i == 0:
        continue
    if 0 <= pos[0] + i <= 7 and 0 <= pos[1] + (3 - abs(i)) <= 7:
        matrix[pos[0] + i][pos[1] + (3 - abs(i))] = '*'
    if 0 <= pos[0] + i <= 7 and 0 <= pos[1] - (3 - abs(i)) <= 7:
        matrix[pos[0] + i][pos[1] - (3 - abs(i))] = '*'

for i in range(8):
    print(*matrix[i])
