a = []
b = ['0', '1', '2']


def check(s):
    d = 0
    for i in s:
        if i == '2':
            d += 1
    if d > len(s) / 2:
        return 1
    return 0


def gen(s):
    if check(s):
        a.append(s)
    if len(s) < 10:
        for i in b:
            gen(s + i)


gen('1')
gen('2')
a = sorted([int(x) for x in a])
t = int(input())
for k in range(t):
    n = int(input())
    for i in range(n):
        print(a[i], end=' ')
    print()
