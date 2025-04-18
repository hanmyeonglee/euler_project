def get_sum_of_aliquots(n: int) -> int:
    sm = 0
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            if i * i == n:
                sm += i
            else:
                sm += i + n // i

    return sm - n

sieve = [True] * 1_000_001
sieve[0] = False
sieve[1] = False

longest_chain = []
longest_chain_set = set()
for num in range(2, len(sieve)):
    if not sieve[num]: continue
    if num in longest_chain_set: continue

    chain = [num]
    chain_set = set(chain)
    while True:
        prev_length = len(chain_set)
        sm = get_sum_of_aliquots(chain[-1])

        if sm > 1_000_000:
            for e in chain:
                sieve[e] = False

            break

        chain.append(sm)
        chain_set.add(sm)

        if sm <= 1 or not sieve[sm]:
            for e in chain:
                sieve[e] = False

            break
        
        if prev_length == len(chain_set):
            ind = chain.index(sm)
            if len(chain) - ind <= len(longest_chain):
                for e in chain:
                    sieve[e] = False
            else:
                for i in range(0, ind):
                    sieve[chain[i]] = False
                
                for e in longest_chain:
                    sieve[e] = False
                
                longest_chain = chain[ind : -1]
                longest_chain_set = set(longest_chain)

            break

print(longest_chain)
print(min(longest_chain))