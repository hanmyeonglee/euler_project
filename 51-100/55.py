def ispal(num):
    num = str(num)
    le = len(num)//2
    if len(num) % 2 == 0:
        return num[:le] == num[le:][::-1]
    else:
        return num[:le] == num[le+1:][::-1]


sm = 0

for n in range(1, 10000):
    cnt = 1
    number = n
    while cnt <= 50:
        number = number + int(str(number)[::-1])
        if ispal(number):
            break
        cnt += 1
    else:
        sm += 1

print(sm)
