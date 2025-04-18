mx = 0
for a in range(1, 100):
    for b in range(1, 100):
        num = a ** b
        sm = sum(map(int, list(str(num))))
        if sm > mx:
            mx = sm

print(mx)
