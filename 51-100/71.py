from math import gcd


def make_fractions(n: int) -> list[float]:
    ret = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            ret.append((i / n, i))
    return ret


def main() -> None:
    all_fractions = []
    for n in range(2, 1000001):
        all_fractions.extend(make_fractions(n))
        if n % 10000 == 0:
            print(f'{n = }')

    all_fractions.sort(key=lambda x: x[0])

    ind = all_fractions.index((3/7, 3))
    print(all_fractions[ind-1][1])


if __name__ == "__main__":
    main()
