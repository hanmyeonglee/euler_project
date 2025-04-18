def triangle_dp(triangle: list[list[int]]) -> int:
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for x, row in enumerate(triangle[1:], 1):
        dp[x][0] = dp[x-1][0] + row[0]

        for y, e in enumerate(row[1:-1], 1):
            dp[x][y] = max(dp[x-1][y-1], dp[x-1][y]) + e

        dp[x][-1] = dp[x-1][-1] + row[-1]

    print(dp[:5])

    return max(dp[-1])


def main() -> None:
    with open('problem\euler\eulerTxt\euler67.txt', 'r') as f:
        triangle = list(
            map(lambda x: list(map(int, x.split())), f.read().splitlines()))
        f.close()

    print(triangle_dp(triangle))


if __name__ == "__main__":
    main()
