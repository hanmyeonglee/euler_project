from typing import Callable
from itertools import permutations as perm


def triangle(x: int) -> int: return x*(x+1)//2
def square(x: int) -> int: return x**2
def pentagonal(x: int) -> int: return x*(3*x-1)//2
def hexagonal(x: int) -> int: return x*(2*x-1)
def heptagonal(x: int) -> int: return x*(5*x-3)//2
def octagonal(x: int) -> int: return x*(3*x-2)


def calculate(x: int, funcs: dict[str, Callable], result: dict[str, dict[int, list[int]]]) -> int:
    cnt = 0
    for name, func in funcs.items():
        res = func(x)
        if 1000 <= res < 10000:
            result[name][res // 100].append(res)
        elif res > 10000:
            cnt += 1
    return cnt


def find_six_cycle_list(result: dict[str, dict[int, list[int]]], targets: list[int], order: list[str], answers: list[int]) -> None:
    if len(targets) == 6:
        if targets[-1] % 100 == targets[0] // 100 and len(set(targets)) == 6:
            answers.append(targets[:])

        return

    prefixes = [targets[-1] % 100] if len(targets) else range(10, 100)
    typ = order[len(targets)]

    for prefix in prefixes:
        if not (10 <= prefix < 100):
            continue

        for num in result[typ][prefix]:
            targets.append(num)
            find_six_cycle_list(result, targets, order, answers)
            targets.pop()


def main() -> None:
    names = ["tri", "sqr", "pnt", "hex", "hpt", "oct"]
    func_names = [triangle, square, pentagonal,
                  hexagonal, heptagonal, octagonal]
    funcs = dict(zip(names, func_names))
    result = {name: {
        prefix: [] for prefix in range(10, 100)
    } for name in names}

    x = 0
    while True:
        cnt = calculate(x, funcs, result)
        if cnt == 6:
            break
        x += 1

    answers = []
    for order in perm(names, 6):
        find_six_cycle_list(result, [], order, answers)

    print(set(map(sum, answers)))


if __name__ == "__main__":
    main()
