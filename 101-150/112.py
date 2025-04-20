def inc(n):
    prev = 10
    while n > 0:
        d = n % 10
        if d > prev: return False
        prev = d
        n //= 10
    
    return True

def dec(n):
    prev = 0
    while n > 0:
        d = n % 10
        if d < prev: return False
        prev = d
        n //= 10

    return True

def is_bouncy(n):
    return not inc(n) and not dec(n)

number = 1
bouncy = 0
while True:
    if is_bouncy(number): bouncy += 1
    if bouncy * 100 % number == 0:
        ratio = bouncy * 100 // number
        if ratio == 99:
            print(number)
            break
    number += 1