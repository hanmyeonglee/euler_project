def combination(n, r):
    sm = 1
    for i, num in enumerate(range(n, n-r, -1), 1):
        sm *= num / i
    return int(sm)


many = 4

for tar in range(24, 101):
    for get in range(4, tar-3):
        if combination(tar, get) > 1000000:
            many += 1

print(many)
