from itertools import permutations, combinations
from getPrimes import get_prime
from time import time

pre_list = []
primes = get_prime(1229)
ans = []


def liner(num):
    return int(''.join(num))


def have_less_4d(L):
    return len(str(L)) == 4


def is_arith(comb):
    return comb[1] - comb[0] == comb[2] - comb[1]


def is_all_prime(comb):
    return comb[0] in primes and comb[1] in primes and comb[2] in primes


tmp = time()
for target in range(1000, 10000):
    if target in pre_list:
        continue
    num_list = list(filter(have_less_4d, map(
        liner, set(permutations(str(target))))))
    comb_list = list(map(sorted, combinations(num_list, 3)))
    for comb in comb_list:
        if is_arith(comb):
            if is_all_prime(comb):
                ans.append(comb)
        pre_list.extend(num_list)

for an in ans:
    if 1487 in an:
        ans.remove(an)

answer = ''.join(list(map(str, ans.pop())))

print(answer)
print(time() - tmp)
