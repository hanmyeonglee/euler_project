import json

L = []
with open('./euler/eulerTxt/euler22.txt', 'r', encoding='utf-8') as f:
    L = sorted(json.loads("["+f.read()+"]"))
fsm = 0
for i in range(len(L)):
    sm = 0
    for j in L[i]:
        sm += ord(j) - 64
    fsm += sm*(i+1)
print(fsm)