import tqdm
from itertools import product

sieve = [True] * 10001
sieve[0] = False
sieve[1] = False

primes = []
for i in range(2, 10001):
    if not sieve[i]: continue
    primes.append(i)
    for j in range(2 * i, 10001, i):
        sieve[j] = False

candidates = [False] * 50_000_000
candidates[0] = False
for x, y, z in tqdm.tqdm(product(primes, repeat=3)):
    num = x ** 2 + y ** 3 + z ** 4
    if num >= 50_000_000: continue
    candidates[num] = True

print(candidates.count(True))