# Напишите программу для расшифровки секретного слова методом частотного анализа.
#
# Формат входных данных
#
# В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре.
# В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.
#
# Формат выходных данных
# Программа должна вывести дешифрованное слово.
#
# Примечание. Гарантируется, что частоты букв не повторяются.


dict_symbols = {}
secret_word = input()
for i in secret_word:
    dict_symbols[i] = dict_symbols.get(i, 0) + 1
dict_letters = {}

for i in range(int(input())):
    letter = input().replace(': ', '')
    dict_letters[letter[0]] = letter[1:]

simbols_keys = list(dict_symbols.keys())
letter_keys = list(dict_letters.keys())
for i in range(len(simbols_keys)):
    secret_word = secret_word.replace(simbols_keys[i], letter_keys[i])
print(secret_word)
