from itertools import permutations as perm


def decrypt(text: list[int], key: list[int]) -> str:
    ret = ''
    for ind, t in enumerate(text):
        ret += chr(t ^ key[ind % 3])
    return ret


def sum_origin_ascii(text: list[int], key: list[int]) -> int:
    ret = 0
    for ind, t in enumerate(text):
        ret += t ^ key[ind % 3]
    return ret


def main() -> None:
    pwords = [' ', '.', 'the', 'and', 'to']
    with open("./problem/euler/eulerTxt/euler59.txt", "r") as f:
        text = list(map(int, f.read().strip().split(",")))
        f.close()

    for key in perm([i for i in range(97, 123)], 3):
        dec_text = decrypt(text, key).lower()
        for pword in pwords:
            if pword not in dec_text:
                break
        else:
            print(dec_text)
            inp = input('continue? : ')
            if inp.lower() == "n":
                print(sum_origin_ascii(text, key))
                print(''.join(map(chr, key)))
                return


if __name__ == "__main__":
    main()
