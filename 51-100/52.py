target = 100

while True:
    origin = set(str(target))
    compare = set(str(target)+str(target*2)+str(target*3) +
                  str(target*4)+str(target*5)+str(target*6))
    if len(origin.difference(compare).union(compare.difference(origin))) == 0:
        print(target)
        break

    target += 1
