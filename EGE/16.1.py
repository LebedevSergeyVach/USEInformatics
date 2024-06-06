# Рекурсия
from functools import lru_cache
from sys import setrecursionlimit

# Лимит глубины рекурсии
setrecursionlimit(1_000_000)


@lru_cache(None)
def f(n):
    if n < 3:
        return 2
    else:
        return 2 * f(n - 2)


print(f(2222/f(2182)))


"""F(n) = n при n < 52;
F(n) = 3 × F(n - 2) - n, если n >= 52.
Чему равно значение выражения F(15127)//F(15099)?"""


def F(n):
    if n < 52:
        return n
    else:
        result = n
        while n >= 52:
            result = 3 * result - n
            n -= 2
        return result


print(F(15127)//F(15099))
