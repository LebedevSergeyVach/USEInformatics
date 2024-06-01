# Функция перевода числа в другую системы счисления (sisi)
def from_10_in_sisi(number: int, sisi: int):
    answer = ""

    while number > 0:
        answer += str(number % sisi)
        number //= sisi

    return answer


# Функция алгоритма
def f(N):
    # R = from_10_in_sisi(N, 2)
    R = bin(N)[2:]

    if N % 3 == 0:
        R = R.replace("0", "11")
    else:
        R = R.replace("1", "10")

    return int(R, 2)


# Укажите максимально число R, которое меньше 161
max_porno = 0

for N in range(1_000_000):
    R = f(N)

    if R < 161:
        max_porno = max(max_porno, R)

print(max_porno)

# Одно из необычных формулировок

def ml_ra(string: str) -> str:
    answer = int(string) % 10

    return str(answer)


def func(N):
    R = bin(N)[2:]

    if R.count('1') % 2 != 0:
        R = R + '1'
    else:
        R = R + '0'

    R = str(int(R, 2))
    R = R + ml_ra(R)

    return int(R)


for N in range(10 ** 10):
    R = func(N)

    if R > 1200:
        print(R)
        break

