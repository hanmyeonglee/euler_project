from isprime import isprime

cnt = 8
num = 49
spiral = 8
while cnt / (1 + 2 * spiral) > 0.1:
    for _ in range(4):
        num += spiral
        if isprime(num):
            cnt += 1
    spiral += 2
print(spiral + 1)
