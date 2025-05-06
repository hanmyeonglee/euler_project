from Crypto.Util.number import isPrime
from tqdm import tqdm

def is_prime(n):
    return isPrime(n)

def is_patterned(n):
    if n % 2 == 1: return False
    if n % 3 == 0: return False
    if n % 7 == 0: return False
    if n % 13 == 0: return False

    n *= n
    return all(is_prime(n + d) for d in (1, 3, 7, 9, 13, 27))

sm = 0
for n in tqdm(range(2, 1_000_000)):
    if is_patterned(n):
        sm += n

print(sm)