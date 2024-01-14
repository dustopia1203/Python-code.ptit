def f(d, n):
    ans = 0
    for i in range(10):
        m = 10 ** i
        if m > n:
            break
        a = n // m
        b = n % m
        z = a % 10
        if z > d:
            ans += ((a // 10) + 1) * m
        elif z == d:
            ans += (a // 10) * m + (b + 1)
        else:
            ans += (a // 10) * m
        if d == 0:
            ans -= m
    return ans


for _ in range(int(input())):
    l, r = map(int, input().split())
    for i in range(10):
        print(f(i, r) - f(i, l - 1), end=' ')
    print()
