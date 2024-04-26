# Маска числа
from fnmatch import fnmatch

mask = '85?16*4'
div = 2658

for i in range(1002066, 10 ** 9 + 1, div):
    if fnmatch(str(i), mask) and i % div == 0:
        print(i, i / div)

# for i in range(10 ** 6, 10 ** 9 + 1):
#     if i % div == 0:#         print(i)
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
