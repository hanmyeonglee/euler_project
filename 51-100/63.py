cnt = 0
for n in range(1, 22):
    for x in range(1, 10):
        res = x**n
        if n == len(str(res)):
            cnt += 1
print(cnt)
