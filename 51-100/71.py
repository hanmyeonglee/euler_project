from math import floor

num = 0
den = 1
for d in range(2, 1_000_001):
    n = floor(3 * d / 7)
    if num * d < den * n and 7 * n < 3 * d:
        num = n
        den = d

print(num)