from sys import stdin

N, mod = 10 ** 6, 10 ** 9 + 7
c = [0] * (N + 1)
c[0] = c[1] = 1
for i in range(4, N + 1, 2):
    c[i] = 1
for i in range(3, N + 1, 2):
    if c[i] == 0:
        for j in range(i * i, N + 1, 2 * i):
            c[j] = 1
del N


def pw(x, y):
    res = 1
    while y != 0:
        if y % 2 == 1:
            res = (res * x) % mod
        y //= 2
        x = (x * x) % mod
    return res


def mu(x, n):
    dem, i = 0, x
    while i <= n:
        dem += n // i
        i *= x
    return dem


for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    ans = 1
    dem = 0
    for i in range(2, b // 2 + 1):
        if c[i] == 0:
            ans = (ans * ((mu(i, b) - mu(i, a - 1)) * 2 + 1)) % mod
    for i in range(b // 2 + 1, b + 1):
        if c[i] == 0:
            dem += 1
    ans = (ans * pw(3, dem)) % mod
    print(ans)
