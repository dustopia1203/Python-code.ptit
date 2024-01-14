f = [0] * 27
for i in range(1, 27):
    f[i] = 2 * f[i - 1] + 1
for _ in range(int(input())):
    n, k = map(int, input().split())
    while n > 1:
        if k == f[n - 1] + 1:
            break
        elif k > f[n - 1] + 1:
            k -= f[n - 1] + 1
            n -= 1
        else:
            n -= 1
    print(chr(ord('A') + n - 1))
