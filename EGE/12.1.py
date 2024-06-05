# Исполнитель с циклом
def sum_numbers(number: int):

    result = 0

    while number > 0:
        result += number % 10
        number //= 10

    return result


def f(str: str) -> str:
    while '1111' in str or '8888' in str:
        if '1111' in str:
            str = str.replace('1111', '88', 1)
        else:
            str = str.replace('8888', '11', 1)

    return str


s = '8' * 45
print(f(s))


def sum_nums(number: int) -> int:
    result = 0

    while number > 0:
        result += number % 10
        number //= 10

    return result


# Второй случай
def func(s: str) -> str:
    while '25' in s or '355' in s or '555' in s:

        if '25' in s:
            s = s.replace('25', '3', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)

    return s


s = ''
for n in range(4, 1000):
    s = '3' + '5' * n
    c = func(s)

    if sum_nums(int(c)) == 27:
        print(n)
        break
