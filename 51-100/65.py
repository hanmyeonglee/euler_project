n = 100

e = [0 for _ in range(n)]
e[0] = 2
x = 1
for i in range(1, n):
    if i % 3 == 2:
        e[i] = x * 2
        x += 1
    else:
        e[i] = 1


z = [0, 1]
for comp in reversed(e):
    z[0] += comp * z[1]
    z[1], z[0] = z[0], z[1]

print(z)
print(sum(map(int, str(z[1]))))
