from itertools import combinations

def is_right_triangle(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2 == 0 \
        or x1 * (x2 - x1) + y1 * (y2 - y1) == 0 \
        or x2 * (x2 - x1) + y2 * (y2 - y1) == 0

# x1, y1 / x2, y2 / 0, 0
# slope1 = (y2 - y1) / (x2 - x1)
# slope2 = y1 / x1
# slope3 = y2 / y2
# 1. x1x2 + y1y2 = 0
# 2. x1*(x2 - x1) + y1*(y2 - y1) = 0
# 3. x2*(x2 - x1) + y2*(y2 - y1) = 0
points = [(x, y) for x in range(51) for y in range(51) if (x, y) != (0, 0)]

cnt = 0
for p1, p2 in combinations(points, 2):
    if is_right_triangle(*p1, *p2):
        cnt += 1

print(cnt)