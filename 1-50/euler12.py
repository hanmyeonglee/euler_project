prime = [2]
sm = 3
inc = 3

def factor(x):
    temp = {}
    for i in range(len(prime)):
        while x % prime[i] == 0:
            x //= prime[i]
            try:
                temp[prime[i]] += 1
            except:
                temp[prime[i]] = 1
        
        if x == 1:
            break
    
    res = 1
    for i in temp.values():
        res *= i+1
    return res

while factor(sm) <= 100:
    sm += inc
    for i in range(sm - inc, sm):
        for j in prime:
            if i % j == 0: break
        else:
            prime.append(i)
    inc += 1

print(sm)