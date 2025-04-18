sm = 0


def exponent(num):
    ex_sm = 1
    for _ in range(num):
        ex_sm *= num
        ex_sm = int(str(ex_sm)[-10:])
    return ex_sm


for num in range(1, 1001):
    sm += exponent(num)
    sm = int(str(sm)[-10:])

print(sm)
