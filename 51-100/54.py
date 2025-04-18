order = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14,
}

suits = {
    "H": 0, "C": 1, "S": 2, "D": 3,
}

masaka = False


class card:
    def __init__(self, information):
        self.value = order[information[0]]
        self.suit = suits[information[1]]
        self.origin = information

    @classmethod
    def cardify(cls, informations):
        ret = []
        for info in informations.split():
            ret.append(cls(info))
        return tuple(ret)


def test_in_draw_state(tar1, tar2):
    assert len(tar1) == len(tar2), "fuck"

    for i in range(len(tar1)):
        if tar1[i] > tar2[i]:
            return True
        elif tar1[i] < tar2[i]:
            return False

    global masaka
    masaka = True
    return False


def test_player1_win(player1, player2, funcs):
    global masaka
    for func in funcs:
        masaka = False
        p1, t1 = func(player1)
        p2, t2 = func(player2)

        if p1 and p2:
            flag = test_in_draw_state(t1, t2)
            if masaka:
                pt = ""
                for c in player1 + player2:
                    pt += c.origin
                print(pt)
            return flag
        else:
            if p1 or p2:
                return p1

    vals1 = [d.value for d in player1]
    vals2 = [d.value for d in player2]

    flag = test_in_draw_state(vals1, vals2)
    if masaka:
        pt = ""
        for c in player1 + player2:
            pt += c.origin
        print(pt)

    return flag


def royal_flush(deck: list[card]):
    crit = deck[0].suit
    vals = [deck[0].value]

    for d in deck[1:]:
        if crit != d.suit:
            return False, None
        else:
            vals.append(d.value)

    vals.sort()

    if vals == [10, 11, 12, 13, 14]:
        return True, vals[::-1]

    return False, None


def straight_flush(deck: list[card]):
    crit = deck[0].suit
    vals = [deck[0].value]

    for d in deck[1:]:
        if crit != d.suit:
            return False, None
        else:
            vals.append(d.value)

    vals.sort()

    for i in range(len(vals)-1):
        if vals[i+1] - vals[i] != 1:
            return False, None

    return True, vals[::-1]


def four_of_a_kind(deck: list[card]):
    vals = {d.value: 0 for d in deck}
    for d in deck:
        vals[d.value] += 1

    for key, value in vals.items():
        if value == 4:
            return True, [key]

    return False, None


def full_house(deck: list[card]):
    vals = {d.value: 0 for d in deck}
    if len(vals) != 2:
        return False, None

    for d in deck:
        vals[d.value] += 1

    if 3 in vals.values():
        ret = [0, 0]
        for key, value in vals.items():
            if value == 3:
                ret[0] = key
            else:
                ret[1] = key
        return True, ret

    return False, None


def flush(deck: list[card]):
    suits = set(d.suit for d in deck)

    if len(suits) == 1:
        return True, sorted([d.value for d in deck], reverse=True)

    return False, None


def straight(deck: list[card]):
    vals = list(map(lambda x: x.value, deck))
    vals.sort()

    for i in range(len(vals)-1):
        if vals[i+1] - vals[i] != 1:
            return False, None

    return True, vals[::-1]


def three_of_a_kind(deck: list[card]):
    vals = {d.value: 0 for d in deck}
    for d in deck:
        vals[d.value] += 1

    for key, value in vals.items():
        if value == 3:
            return True, [key]

    return False, None


def two_pairs(deck: list[card]):
    vals = {d.value: 0 for d in deck}
    if len(vals) != 3:
        return False, None

    for d in deck:
        vals[d.value] += 1

    ret = []
    for key, value in vals.items():
        if value == 2:
            ret.append(key)

    if len(ret) == 2:
        return True, sorted(ret, reverse=True)

    return False, None


def one_pair(deck: list[card]):
    vals = {d.value: 0 for d in deck}

    for d in deck:
        vals[d.value] += 1

    for key, value in vals.items():
        if value == 2:
            return True, [key]

    return False, None


def high_card(deck: list[card]):
    return True, [max(d.value for d in deck)]


stages = []
with open("./problem/euler/eulerTxt/euler54.txt", "r") as file:
    for line in file.readlines():
        # print(line[:15], line[16:], sep="|||")
        p1, p2 = card.cardify(line[:14]), card.cardify(line[15:])
        stages.append((p1, p2))

win_player1 = 0
funcs = [royal_flush, straight_flush, four_of_a_kind, full_house,
         flush, straight, three_of_a_kind, two_pairs, one_pair, high_card]
for stage in stages:
    p1, p2 = stage
    if test_player1_win(p1, p2, funcs):
        win_player1 += 1

print("number of win of player1 : %d" % win_player1)
