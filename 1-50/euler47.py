from getPrimes import get_prime

target = 2
primes = get_prime(100000)


def factorization(x):
    i = 0
    typ = set()
    while x > 1:
        p = primes[i]
        if x % p == 0:
            x //= p
            typ.add(p)
        else:
            i += 1
    return len(typ)


stack = []
while True:
    if factorization(target) == 4:
        stack.append(target)
    else:
        stack.clear()

    if len(stack) == 4:
        print(stack)
        break

    target += 1
