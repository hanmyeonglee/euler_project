from math import sqrt

"""target = 35
primes = []

with open('./primelists/100000primes/primes.0000', 'r') as f:
    f.readline()
    while True:
        prime = int(f.readline())
        flag = False

        if prime <= target:
            target += 2
            primes.append(prime)
        else:
            while True:
                flag01 = False
                for p in primes:
                    tmp = sqrt((target - p)/2)
                    if tmp - int(tmp) != 0:
                        print(target)
                        flag = True
                        flag01 = True
                        break
                if flag01:
                    break
                target += 2
                if target >= prime:
                    primes.append(prime)
                    break

        if flag:
            break
    f.close()
 """
target = 35
num = 10000
primes = []

with open('./primelists/100000primes/primes.0000', 'r') as f:
    for _ in range(num):
        primes.append(int(f.readline()))
    f.close()

print('fin')

while True:
    flag = True
    if target in primes:
        target += 2
        continue
    for p in primes:
        if p >= target:
            break
        red = target - p
        tmp = sqrt(red/2)
        if tmp - int(tmp) == 0:
            flag = False
            break

    if flag:
        print(target)
        break
    target += 2
