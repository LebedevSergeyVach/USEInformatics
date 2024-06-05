from random import randint


def fate(word: str) -> str:
    if randint(0, 1) == 0:
        word += '++'
    else:
        word += 'ЕКС'

    return word


if __name__ == '__main__':
    print(fate('С'))
