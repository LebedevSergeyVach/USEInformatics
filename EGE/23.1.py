# Динамическое программирование
def func(position: int, destination: int, command: str) -> int:
    if position > destination:
        return 0
    if position == destination:
        return 1

    if command == 'B':
        return func(position + 2, destination, 'A') + func(position * 3, destination, 'C')

    return func(position + 2, destination, 'A') + func(position ** 2, destination, 'B') + func(position * 3, destination, 'C')


print(func(2, 64, ''))
