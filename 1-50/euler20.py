fact = 1

for i in range(1, 101):
    fact *= i
    while fact % 10 == 0:
        fact //= 10

print(fact)
print(sum(list(map(int, list(str(fact))))))