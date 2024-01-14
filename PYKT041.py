from math import comb


n = int(input())
a = []
for i in range(n):
    a.append([i for i in input()])
res = 0
for i in range(n):
    v = 0
    h = 0
    for j in range(n):
        if a[i][j] == 'C':
            v += 1
        if a[j][i] == 'C':
            h += 1
    res += comb(v, 2)
    res += comb(h, 2)
print(res)
