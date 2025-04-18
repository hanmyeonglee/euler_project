def phi_function(n: int) -> int:
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1

    if n > 1:
        result -= result // n

    return int(result)


def isperm(x: int, y: int) -> bool:
    x, y = map(lambda x: list(sorted(list(str(x)))), (x, y))
    return x == y


def main() -> None:
    mn_n, mn_val = 0, 10 ** 7

    for n in range(2, 10 ** 7):
        phi = phi_function(n)

        if not isperm(n, phi):
            continue

        res = n / phi
        if mn_val > res:
            mn_n, mn_val = n, res

    print(mn_n)


if __name__ == "__main__":
    main()
