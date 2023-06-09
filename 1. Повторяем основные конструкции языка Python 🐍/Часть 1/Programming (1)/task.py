# Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. ИМТ показывает весит человек больше
# или меньше нормы для своего роста. ИМТ человека рассчитывают по формуле:
#
# ИМТ=масса(кг)/(рост(м)×рост(м)),
#
# где масса измеряется в килограммах, а рост — в метрах.
#
# Масса человека считается оптимальной, если его ИМТ находится между 18.5 и 25. Если ИМТ меньше 18.5, то считается,
# что человек весит ниже нормы. Если значение ИМТ больше 25, то считается, что человек весит больше нормы.
#
# Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно). "Недостаточная
# масса", если ИМТ меньше 18.5 и "Избыточная масса", если значение ИМТ больше 25.
#
# Формат входных данных На вход программе подается два числа: масса и рост человека, каждое на отдельной строке. Все
# входные числа являются вещественными, используйте для них тип данных float.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.


f_mass, f_height = float(input()), float(input())
if (f_mass / (f_height * f_height)) < 18.5:
    print("Недостаточная масса")
elif (f_mass / (f_height * f_height)) > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")
