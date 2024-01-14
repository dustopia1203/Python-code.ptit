def check(n, m):
    _n = ""
    while n > 0:
        _n += str(n % m)
        n //= m
    return _n == _n[::-1]


def check_bin(n):
    tmp = bin(n)[2:]
    return tmp == tmp[::-1]


a, b, m = map(int, input().split())
res = [i for i in range(a, b + 1) if check_bin(i)]
for k in range(3, m + 1):
    res = [i for i in res if check(i, k)]
print(len(res))
