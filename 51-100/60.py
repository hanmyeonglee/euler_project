def isprime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True


def sieve_of_erathosthenes(max: int) -> list[bool]:
    ret = [True for _ in range(max + 1)]
    ret[0] = False
    ret[1] = False
    for i in range(2, max + 1):
        if ret[i]:
            for j in range(i * 2, max + 1, i):
                ret[j] = False
    return ret


def get_primes_from_sieve(sieve: list[bool], max: int) -> list[int]:
    ret = []
    for num, flag in enumerate(sieve):
        if flag and num <= max:
            ret.append(num)

    return ret


def test_two_element(p1: int, p2: int, sieve: list[bool]) -> bool:
    prime1 = int(str(p1) + str(p2))
    prime2 = int(str(p2) + str(p1))
    flag1 = sieve[prime1] if len(sieve) >= prime1 else isprime(prime1)
    flag2 = sieve[prime2] if len(sieve) >= prime2 else isprime(prime2)
    return flag1 and flag2


def find_concatenatable_primes(primes: list[int], targets: list[int], goal: int, sieve: list[int]) -> int:
    if len(targets) == goal + 1:
        return sum(targets)

    ret = [0]
    for p in primes:
        for pp in targets:
            if not test_two_element(p, pp, sieve):
                break
        else:
            ret.append(
                find_concatenatable_primes(
                    primes, targets + [p], goal, sieve
                )
            )

    return min(ret)


def main(digit: int) -> None:
    max = 10 ** (digit + 1) - 1
    sieve = sieve_of_erathosthenes(max)
    primes = get_primes_from_sieve(sieve, 10 ** (digit // 2))
    minimum = find_concatenatable_primes(primes, [], 5, sieve)
    print(minimum)


if __name__ == "__main__":
    main(8)
