from math import sqrt, floor, ceil
import tqdm

# n x m일 떄 총 rectangle 개수는 nm(n+1)(m+1) / 4
# 이게 2000000과 비슷해야함
# 즉 nm(n+1)(m+1) = 8000000 = 2 ** 9 * 5 ** 6

def get_rect_n(n, m):
    return n * m * (n + 1) * (m + 1) // 4

area = 0
diff = 2000000
for n in tqdm.tqdm(range(1, 2001)):
    for m in range(1, 2001):
        rect_value = get_rect_n(n, m)
        D = abs(rect_value - 2000000)
        if D < diff:
            area = n * m
            diff = D
            if rect_value > 2000000:
                break

print(area)