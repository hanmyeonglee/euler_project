S = set(range(1, 10))

def both(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    
    return set(digits[:9]) == S and set(digits[-9:]) == S

a = 0
b = 1
i = 1
while True:
    if both(b):
        print(i)
        break

    a, b = b, a + b
    i += 1