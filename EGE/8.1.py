from itertools import *


from itertools import *

c = 0
for i in product('myka', repeat=6):
    i = ''.join(i)
    # if (i[0] == 'm' or i[0] == 'k') and (i[-1] == 'y' or i[-1] == 'a'):
    if i[0] in 'mk' and i[-1] in 'ya':
        c += 1

print(c)


from itertools import *

c = 0
for i in product('moda', repeat=4):
    i = ''.join(i)
    if i.count('m') == 1 and i.count('o') == 1 and i.count('d') == 1 and i.count('a') == 1 and \
        'oa' not in i and 'md' not in i and 'ao' not in i and 'dm' not in i:
        c += 1
        print(i)
print(c)


# c = 0
# for i in product('baron', repeat=5):
#     i = ''.join(i)
#     if 'ar' not in i and i[0] != 'a' and i.count('b') == 1 and i.count('a') == 1 and i.count('r') == 1 \
#             and i.count('o') == 1 and i.count('n') == 1:
#         c += 1
#         print(i)
# print(c)


# c = 0
# for i in product('АБВГЭЮЯ', repeat=4):
#     i = ''.join(i)
#     if (i[0] == 'А' or i[0] == 'В' or i[0] == 'Э') and (i[-1] == 'А' or i[-1] == 'В' or i[-1] == 'Э') \
#             and i[1] != 'А' and i[1] != 'В' and i[1] != 'Э' and i[2] != 'А' and i[2] != 'В' and i[2] != 'Э':
#         print(i)
#         c += 1
#
# print(c)


# c = 0
# for i in product('АПРСУ', repeat=3):
#     c += 1
#     if ''.join(i) == 'РАА':
#         print(c)


# counter = 0
# for i in product('школа', repeat=3):
#     i = ''.join(i)
#     if i.count('к') == 1:
#         counter += 1
#         print(i)
#
# print(counter)
