def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


days = {
    "Jan": 31,
    "Feb": 28,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31,
}

date = 0
sm = 0

for y in range(1900, 2001):
    leap = is_leap(y)
    for mon in days.keys():
        d = days[mon]

        if mon == "Feb" and leap:
            d += 1

        if date == 6 and y >= 1901:
            sm += 1

        date += d % 7
        date %= 7

print(sm)
