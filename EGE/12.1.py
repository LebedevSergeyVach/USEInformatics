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
