def calc(n):
    ret = 0
    while n > 0:
        ret += (n % 10) ** 2
        n //= 10

    return ret

s1 = set([1])
s89 = set([89])
cnt = 0
for N in range(1, 10 + 1):
    s = set()
    s.add(N)
    while True:
        nxt = calc(N)
        if nxt in s1:
            s1.update(s)
            break

        if nxt in s89:
            s89.update(s)
            cnt += 1
            break
        
        s.add(nxt)
    
print(s1)
print(s89)
print(cnt)