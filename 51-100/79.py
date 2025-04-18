import copy

passcode = 319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716
matrix = [[0] * 10 for _ in range(10)]
for code in passcode:
    a, b, c = code // 100, code // 10 % 10, code % 10
    matrix[a][b] += 1
    matrix[b][c] += 1

print("  0 1 2 3 4 5 6 7 8 9")
for i, row in enumerate(matrix):
    print(i, end=' ')
    for e in row:
        print(e, end=' ')
    print()