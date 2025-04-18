L = [str(i) for i in range(0, 10)]
cnt = 0

def permute(crit, state):
    global cnt
    if len(crit) == 0:
        cnt += 1
        if cnt == 1000000:
            print(state)
    for i in range(0, len(crit)):
        permute(crit[:i]+crit[i+1:], state+crit[i])

permute(L, "")