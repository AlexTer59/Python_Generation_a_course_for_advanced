# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.


from decimal import *

num = Decimal(input())
if '0' in str(num):
    print(max(num.as_tuple().digits))
else:
    print(max(num.as_tuple().digits) + min(num.as_tuple().digits))
