import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if check(i):
        b.append(i)
b.sort()
pivot = 0
for i in a:
    if check(i):
        print(b[pivot], end=' ')
        pivot += 1
    else:
        print(i, end=' ')
print()
