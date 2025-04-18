def sort_three_integer(a: int, b: int, c: int) -> tuple[int]:
    ret = [a, b, c]
    ret.sort()
    return tuple(ret)


def is_triangle(a: int, b: int, c: int) -> bool:
    return a ** 2 + b ** 2 == c ** 2


def main() -> None:
    N = 1500000
    abc_range = range(1, 1225)
    result = [0 for _ in range(N + 1)]
    dp_set = set()
    for a in abc_range:
        for b in abc_range:
            if a + b >= N:
                break

            for c in abc_range:
                sm = a + b + c
                if sm > N:
                    break

                int3 = sort_three_integer(a, b, c)
                if int3 in dp_set:
                    continue

                x, y, z = int3
                if is_triangle(x, y, z):
                    result[sm] += 1

                dp_set.add(int3)

    cnt = 0
    for res in result:
        if res == 1:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
