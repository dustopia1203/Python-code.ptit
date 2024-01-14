import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if i not in b:
        b.append(i)
s1 = 0
s = sum(b)
res = -1
for i in range(len(b)):
    s1 += b[i]
    if check(s1) and check(s - s1):
        res = i
        break
print(res if res > -1 else "NOT FOUND")
