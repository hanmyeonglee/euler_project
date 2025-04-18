f_2 = 1
f_1 = 1
f_c = None
cnt = 1
while len(str(f_c)) < 1000:
    cnt += 1
    f_c = f_1 + f_2
    f_2 = f_1
    f_1 = f_c
print(cnt)