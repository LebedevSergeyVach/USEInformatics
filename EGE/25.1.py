# Маска числа
from fnmatch import fnmatch

mask = '85?16*4'
div = 2658

for i in range(1002066, 10 ** 9 + 1, div):
    if fnmatch(str(i), mask) and i % div == 0:
        print(i, i / div)

# for i in range(10 ** 6, 10 ** 9 + 1):
#     if i % div == 0:
#         print(i)
#         break


# Второй случай
from fnmatch import fnmatch

mask = '*6215'
div = 23


def max_div(num: int) -> int:
    for i in range(num - 1, 0, -1):
        if num % i == 0:
            return i


for i in range(10005, 10 ** 6 + 1, div):
    d = max_div(i)
    if fnmatch(str(d), mask):
        print(i, d)


# Второй способ
from fnmatch import fnmatch

# маска и делитель
mask = '12?3*46'
div = 129

# Нахождение промежутка
for i in range(10 ** 6, 10 ** 9 + 1):
    if i % div == 0:
        print(i)
        break

# Нахождение всех чисал маски
for i in range(1000008, 10 ** 8 + 1, div):
    if fnmatch(str(i), mask) and i % div == 0:
        print(i, i // div)


from fnmatch import fnmatch


mask = '*18??18'
div_one = 18
div_two = 1018


def count_div(number: int) -> int:
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    return count


for i in range(1, 10**9 + 1):
    if i % div_one == 0 and i % div_two == 0:
        # print(i)
        break # 9162


for i in range(1, 10**9 + 1):
    if fnmatch(str(i), mask) and i % div_one == 0 and i % div_two == 0:
        print(i, count_div(i))
