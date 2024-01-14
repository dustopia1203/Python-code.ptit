from itertools import *


for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(i)
    d = list(permutations(a))
    d.reverse()
    print(len(d))
    for i in d:
        print(*i, sep='', end=' ')
    print()
