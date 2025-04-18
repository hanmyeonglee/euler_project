from isprime import isprime
from getPrimes import get_prime


class tmp:
    def __init__(self, number, left, right):
        self.number = number
        self.left = left
        self.right = right


primes = get_prime(1229)
target = {}
answer = 0

sm = 0
for i, p in enumerate(primes):
    if sm + p >= 1000000:
        target = tmp(sm, 0, i-1)
        break
    else:
        sm += p


def next_list():
    target.number -= primes[target.left]
    target.left += 1
    if target.right + 1 > 1228:
        return
    if target.number + primes[target.right + 1] < 1000000:
        target.number += primes[target.right + 1]
        target.right += 1


while True:
    if isprime(target.number):
        temp = target.right - target.left
        if temp > answer:
            print(f"{target.number} : {target.left} ~ {target.right}")
            answer = temp
    next_list()
    if target.number == 0:
        break

print(answer)
