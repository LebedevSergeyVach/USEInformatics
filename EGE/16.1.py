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
