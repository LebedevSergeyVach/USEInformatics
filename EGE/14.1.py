# пример
x = 5 * 216**1225 + 4 * 36**1256 - 4 * 6**1257 - 2023

s = ''
while x != 0:
    # 6 - система счисления
    s += str(x % 6)
    x //= 6

s = s[::-1]
# 5 - искомое число
print(s.count("5"))