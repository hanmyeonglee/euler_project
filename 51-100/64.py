from gmpy2 import iroot


def find_cycle_length(x: int) -> int:
    a, b, c = 1, x, int(x ** 0.5)
    s = set()
    while True:
        z = int(a / (b ** 0.5 - c))
        a = (b - c**2) // a
        c = abs(c - z * a)

        length = len(s)
        s.add((a, b, c))
        if length == len(s):
            return length


cnt = 0
for x in range(2, 10001):
    if not iroot(x, 2)[1]:
        length = find_cycle_length(x)
        if length % 2:
            cnt += 1
print(cnt)
