from math import sqrt

def isprime(x):
    if x % 2 == 0 or x % 3 == 0:
        return False
    inc = 4
    for i in range(5, int(sqrt(x))+1, inc):
        inc = 6 - inc
        if x % i == 0:
            return False
    else:
        return True

L = [True for _ in range(0, 13000)]
L[0] = False
L[1] = False
prime_list = []
mx = 0
tup = ()

print("Stage 01 Success")

for num in range(0, len(L)):
    if L[num]:
        j = 2
        while num * j < len(L):
            L[num * j] = False
            j += 1
        prime_list.append(num)

print("Stage 02 Success :", len(prime_list))

for a in range(-1000, 1001):
    if a == 0:
        print("Stage 03 Success :", tup, mx)
        continue

    for b in range(0, 1001):
        if b not in prime_list: continue

        cnt = 0
        n = 0

        while True:
            target = n**2 + a*n + b

            if target not in prime_list:
                break

            n += 1
        
        if n > mx:
            mx = n
            tup = (a, b)

print("Stage 04 Success")
print(tup, mx)