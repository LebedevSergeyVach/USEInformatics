from itertools import product, permutations


def f(x, y, w, z):
    return int( (x or y) and (not (y == z)) and (not w) )


for x1, x2, x3 in product([0, 1], repeat=3):
    t = (
        (1, x1, 1, x2, 1),
        (0, 1, x2, 0, 1),
        (x3, 1, 1, 0, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations('xywz', r=4):
            if all( f ( **dict ( zip (p, r) ) ) == r[-1] for r in t ):
                print(p)


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
