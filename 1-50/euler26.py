def recip(x):
    L = []
    target = 1
    while True:
        target = target * 10 % x
        for ind, t in enumerate(L):
            if t == target:
                return len(L) - ind
        if target == 0:
            return 0
        L.append(target)


mx = 0
mx_n = 0
for i in range(1, 1001):
    n = recip(i)
    if n > mx:
        mx_n = i
        mx = n
print(mx_n)
