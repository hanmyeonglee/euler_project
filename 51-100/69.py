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


def main() -> None:
    mx_val = 0
    mx_n = 0
    for n in range(2, 1000001):
        phi = phi_function(n)
        res = n / phi

        if res > mx_val:
            mx_n, mx_val = n, res

    print(mx_n)


if __name__ == "__main__":
    main()
