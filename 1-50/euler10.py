L = [True for i in range(2000001)]
L[0] = False
L[1] = False

for i in range(2, len(L)):
    if L[i]:
        j = 2
        while i*j < len(L):
            L[i*j] = False
            j += 1

sm = 0
for i in range(len(L)):
    if L[i]:
        sm += i
print(sm)