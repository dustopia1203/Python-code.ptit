MOD = 10 ** 9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    res = 0
    p = 1
    while k > 0:
        if k & 1:
            res += p
            res %= MOD
        p *= n
        k >>= 1
    print(res)
