mx = 0
res = 0
for i in range(1, 1000000):
    cnt = 0
    target = i
    while target > 1:
        cnt += 1
        if target % 2 == 0:
            target //= 2
        else:
            target = target*3 + 1
    if(cnt > mx):
        mx = cnt
        res = i

print(res, mx)