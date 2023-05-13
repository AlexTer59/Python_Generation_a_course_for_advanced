# Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и
# строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.
#
# Формат входных данных
# На вход программе подаётся одна строка текста.
#
# Формат выходных данных
# Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.


import string


def is_valid_password(password):
    return 'YES' if len(password) >= 7 and all((any(map(lambda x: x in (string.digits), password)),
                                                any(map(lambda x: x in (string.ascii_lowercase), password)),
                                                any(map(lambda x: x in (string.ascii_uppercase), password)))) else 'NO'


pasword = input()
print(is_valid_password(pasword))
