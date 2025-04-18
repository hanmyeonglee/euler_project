from math import sqrt

a = 286
while True:
    b = (1+sqrt(1+12*a**2+12*a))/6
    c = (1+sqrt(1+4*b**2+4*b))/4
    if b - int(b) == 0 and c - int(c) == 0:
        print("a's value :", a)
        print("answer :", a*(a+1)/2)
        break
    a += 1
