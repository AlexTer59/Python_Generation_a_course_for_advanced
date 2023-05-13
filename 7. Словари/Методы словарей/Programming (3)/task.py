# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
# должно быть выведено то, что меньше в лексикографическом порядке.


s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

l_s = s.split()
result = {}
max = 0
for i in l_s:
    result[i] = result.get(i, 0) + 1
for key, value in result.items():
    if max < value:
        max = value
print(min({i for i in result if result[i] == max}))
