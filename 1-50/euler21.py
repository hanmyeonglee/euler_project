from math import sqrt

def summation(x):
    sm = 1
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            sm += i
            sm += x // i
    return sm

set = {i:summation(i) for i in range(2, 10001)}
cnt = 0

m = 0
for key in range(2, 10001):
    a, b = key, set.get(key)
    if (a != b) and 2 <= b and b <= 10000:
        if set.get(b) == a:
            m += a

print(m)