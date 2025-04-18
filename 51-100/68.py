from itertools import combinations as comb


def make_decagon() -> list[int]:
    s = set([i + 1 for i in range(10)])
    s1 = list(comb(s, 5))
    for elements in s1:
        s2 = list(s - set(elements))
