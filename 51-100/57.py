from fractions import Fraction


def reciprocal(number: Fraction):
    return Fraction(number.denominator, number.numerator)


sm = 0
one = Fraction(1, 1)
num = Fraction(3, 2)
for _ in range(999):
    num += one
    num = reciprocal(num)
    num += one

    nu, de = str(num.numerator), str(num.denominator)
    if len(nu) > len(de):
        sm += 1
print(sm)
