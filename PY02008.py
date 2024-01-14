import math

p = [1] * 10001
p[0] = p[1] = 0
for i in range(2, int(math.sqrt(10001)) + 1):
    if p[i] == 1:
        for j in range(i * i, 10001, i):
            p[j] = 0
a = []
for i in range(10001):
    if p[i] == 1:
        a.append(i)
n, x = map(int, input().split())
cnt = 0
print(x, end=' ')
while n > 0:
    x += a[cnt]
    print(x, end=' ')
    cnt += 1
    n -= 1