# xy = n * (x + y)
# y(x - n) = nx
# y = nx / (x - n)
# y = (n, n * (n + 1)]

n = 5
while True:
    cnt = 0
    x = n + 1
    while True:
        num = n * x
        den = x - n
        if num % den == 0:
            if x // den < 2: break
            cnt += 1
        x += 1
    if cnt > 1000:
        print(n)
        break

    n += 1