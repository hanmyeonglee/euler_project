def fact(a, b):
    goal = a+b
    sm = 1
    res = []
    for i in range(1, goal+1):
        sm *= i
        if i == a:
            res.append(sm)
        if i == b:
            res.append(sm)
    res.append(sm)
    return res

a, b= map(int, input("a,b:").split(","))
result = fact(a, b)
print(result[2]//(result[1]*result[0]))