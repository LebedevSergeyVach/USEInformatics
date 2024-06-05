# Одна куча с говном
def func(s, m):
    if s >= 301:
        return not (m % 2)
    if m == 0:
        return 0

    hods = [func(s + 3, m -1), func(s * 5, m -1)]

    return any(hods) if m % 2 else all(hods)


print(f'19 => {min([s for s in range(1, 301) if (not func(s, 1)) and func(s, 2)])}')
print(f'20 => {[s for s in range(1, 301) if (not func(s, 1)) and func(s, 3)]}')
print(f'21 => {min([s for s in range(1, 301) if (not func(s, 2)) and func(s, 4)])}')


# Две кучки с какашками
# s - кол-во камней
# m - ход
def f(a, b, m):
    if a * b >= 777: return not (m % 2)
    if m == 0: return 0

    h = [f(a + 3, b, m - 1), f(a, b + 3, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]

    return any(h) if (m % 2) else all(h)


# a = 7
# print('19)', min([b for b in range(1, 111) if f(7, b, 2)]))  # поменяли all на any при "неудачном ходе"

# наим и наиб
print('20)', [b for b in range(1, 111) if (not f(7, b, 1)) and f(7, b, 3)])  # поменяли обратно

print('21)', [b for b in range(1, 111) if (not f(7, b, 2)) and f(7, b, 4)])


"""def func(s, m):
    if s >= 435:
        return not (m % 2)
    if m == 0:
        return 0

    hods = [func(s + 5, m - 1), func(s * 3, m - 1)]

    return any(hods) if m % 2 else all(hods)


print(f'19 => {min([s for s in range(1, 435) if (not func(s, 1)) and func(s, 2)])}')
print(f'20 => {sorted([s for s in range(1, 435) if (not func(s, 1)) and func(s, 3)])}')
print(f'21 => {min([s for s in range(1, 435) if (not func(s, 2)) and func(s, 4)])}')
"""


"""def func(s, m):
    if s >= 512:
        return not (m % 2)
    if m == 0:
        return 0

    hods = [func(s + 2, m - 1), func(s + 3, m - 1), func(s + 4, m - 1),
            func(s + 5, m - 1), func(s * 2, m - 1)]

    return any(hods) if m % 2 else all(hods)


print(f'19 => {max([s for s in  range(1, 512) if (not func(s, 1)) and func(s, 2)])}')
print(f'20 => {sorted([s for s in range(1, 512) if (not func(s, 1)) and func(s, 3)])}')
print(f'21 => {min([s for s in range(1, 512) if (not func(s, 2)) and func(s, 4)])}')
"""