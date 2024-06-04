from itertools import product, permutations


def func(x, y, z, w):
    return (x or ((not z) and w) or w) == (y and (not x) and w)


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    tabl = (
        (1, x1, x2, 0, 1),
        (1, x3, 0, 0, 1),
        (0, 1, x4, 1, 1)
    )

    if len(tabl) == len(set(tabl)):
        for permut in permutations('xyzw', r=4):
            if all(func(**dict(zip(permut, r))) == r[-1] for r in tabl):
                print(permut)


# Второй базовый вариант для составления таблицы истинности
print('x y z w F')


def func(x, y, z, w):
    return (x and (not y)) or (y == z) or w


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if func(x, y, z, w) == 0:
                    print(f'{x} {y} {z} {w} {func(x, y, z, w)}')
