def pentagonal():
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        n += 1

def pentagonal_pair():
    n = 1
    while True:
        yield n * (3 * n + 1) // 2
        n += 1

cache = [1]
p1 = list()
p2 = list()

g1 = pentagonal()
g2 = pentagonal_pair()

next1 = next(g1)
next2 = next(g2)

number = 1
while True:
    if number >= next1:
        p1.append(next1)
        next1 = next(g1)
    
    if number >= next2:
        p2.append(next2)
        next2 = next(g2)
    
    sign = 1
    pn = 0
    for n1 in p1:
        pn += sign * cache[number - n1]
        sign *= -1
    
    sign = 1
    for n2 in p2:
        pn += sign * cache[number - n2]
        sign *= -1

    cache.append(pn)
    if pn % 1_000_000 == 0:
        break

    number += 1

print(number)