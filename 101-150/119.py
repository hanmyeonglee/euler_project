import tqdm

def sum_digit(num):
    ret = 0
    while num > 0:
        ret += num % 10
        num //= 10
    return ret

length = 20
MAX = int('9' * length)
MAX_SM = 9 * length

L = []
for num in tqdm.tqdm(range(2, MAX_SM + 1)):
    sm = num
    while sm < MAX:
        if sum_digit(sm) == num and sm > 10:
            L.append(sm)
        sm *= num

L.sort()
print(L[29])