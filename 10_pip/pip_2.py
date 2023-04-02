def peshroll(m: int, n: int) -> int:
    F = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = F[i - 1][j] + F[i - 1][j - 1] + F[i][j - 1]

    ll = len(str(F[-1][-1])
    print("-" * (ll + m * 2 + 1))
    for i in F:
        for j in F:
            print(end="|")
            print(end=str(j) + "|")
    print("\n" + "-" * (m * 3 + 1))

    return F[n - 1][m - 1]

print(peshroll(5, 5))