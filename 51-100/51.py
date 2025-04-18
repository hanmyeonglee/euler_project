from itertools import combinations as comb, combinations_with_replacement as combwr


def list_to_int(lst: list[int]) -> int:
    return int(''.join(map(str, lst)))


def sieve_of_erathosthenes(max: int) -> list[bool]:
    ret = [True for _ in range(max + 1)]
    ret[0] = False
    ret[1] = False
    for i in range(2, max + 1):
        if ret[i]:
            for j in range(i * 2, max + 1, i):
                ret[j] = False
    return ret


def count_based_on_form(form: list[int], sieve: list[int], inds: list[int]) -> int:
    cnt = 0
    start = 1 if 0 in inds else 0
    for i in range(start, 10):
        for ind in inds:
            form[ind] = i
        num = list_to_int(form)

        if sieve[num]:
            cnt += 1

    return cnt


def make_next(lst: list[int]):
    for e in lst:
        yield e


def main(digit: int) -> None:
    max = 10 ** (digit + 1) - 1
    sieve = sieve_of_erathosthenes(max)
    for inds in comb([i for i in range(digit)], 3):
        for nums in combwr([i for i in range(10)], 3):
            numbers = make_next(nums)
            form = [0 if i in inds else next(numbers) for i in range(digit)]

            print(list_to_int(form), end=' ')
            cnt = count_based_on_form(form, sieve, inds)

            if cnt == 8:
                print('success')
                return
            else:
                print('failed')


if __name__ == "__main__":
    main(6)
