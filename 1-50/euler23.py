from math import sqrt

def summation(x):
    sm = 1
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            sm += i
            if i != x//i:
                sm += x//i

    if sm > x:
        return True
    else:
        return False

expect = set(i for i in range(0, 28124))
abundant = list(filter(summation, [i for i in range(1, 28124)]))

for i in abundant:
    for j in abundant:
        target = i + j
        if target in expect:
            expect.remove(target)

print(sum(expect))