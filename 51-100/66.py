from gmpy2 import iroot
from typing import Iterator
from time import sleep


def issqrt(x: int) -> bool:
    return iroot(x, 2)[1]


def find_cycle(x: int) -> list[tuple[int, int, int]]:
    a, b, c = 1, x, int(x ** 0.5)
    s = set()
    ret = []
    while True:
        length = len(s)
        s.add((a, b, c))
        if length == len(s):
            return ret

        ret.append((a, b, c))

        z = int(a / (b ** 0.5 - c))
        a = (b - c**2) // a
        c = abs(c - z * a)


def calc_fraction(sentence: list[int]) -> list[int, int]:
    z = [0, 1]
    for comp in reversed(sentence):
        z[0] += comp * z[1]
        z[1], z[0] = z[0], z[1]

    return z[::-1]


def fraction_generator(start: int, cycle: list[int]) -> Iterator[list[int, int]]:
    sentence = [start]
    z = calc_fraction(sentence)

    ind = 0
    length = len(cycle)
    while True:
        yield z
        sentence.append(cycle[ind % length])
        z = calc_fraction(sentence)
        ind += 1


def is_result_1(xy: list[int], D: int) -> bool:
    x, y = xy
    return x ** 2 - D * y**2 == 1


def main() -> None:
    mx_x = 0
    mx_D = 0
    for D in range(2, 1001):
        if issqrt(D):
            continue

        start = int(iroot(D, 2)[0])
        cycle = []
        for a, b, c in find_cycle(D):
            cycle.append(int(a / (b ** 0.5 - c)))

        generator = fraction_generator(start, cycle)
        while not is_result_1(tmp := next(generator), D):
            continue

        x = tmp[0]
        if x > mx_x:
            mx_x = x
            mx_D = D

        print(f'{D = }, {mx_D = }, {mx_x = }')

    print(mx_D)


if __name__ == "__main__":
    main()
