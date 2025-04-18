def test():
    for b in range(2, 1000):
        for a in range(1, b):
            c = 1000 - a - b
            if c**2 == a**2 + b**2:
                print(a,b,c,a*b*c)
                return
            else:
                continue


test()