def rearrangement(x: int):
    ret = list(str(x))
    ret.sort()
    return ''.join(ret)


def main() -> None:
    x = 0
    result = {}
    while True:
        res = rearrangement(x ** 3)
        result[res] = result.get(res, []) + [x ** 3]

        if len(result[res]) == 5:
            print(min(result[res]))
            return

        x += 1


if __name__ == "__main__":
    main()
