# Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
#
# Напишите программу сортировки списка спортсменов по указанному полю:
#
# 1: по имени;
# 2: по возрасту;
# 3: по росту;
# 4: по весу.
# Формат входных данных
# На вход программе подается натуральное число от 1 до 4 – номер поля по которому требуется отсортировать список.
#
# Формат выходных данных
# Программа должна вывести отсортированный по заданному полю список в соответствии с примерами.
#
# Примечание. Решите задачу без использования условного оператора.


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def comporator(athletes):
    return athletes[n - 1]


n = int(input())
for i in (sorted(athletes, key=comporator)):
    print(*i)
