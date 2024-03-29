import math as mt


def nt(n):
    if n < 2:
        return 0
    if n <= 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    for i in range(5, int(mt.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return 0
    return 1


def cs(n):
    s = 0
    while n:
        r = n % 10
        if nt(r) == 0:
            return 0
        s += r
        n //= 10
    return nt(s)


t = int(input())
for k in range(0, t):
    n = int(input())
    t = str(n)
    t = t[::-1]
    t = int(t)
    if nt(n) and cs(n) and nt(t):
        print('Yes')
    else:
        print('No')
