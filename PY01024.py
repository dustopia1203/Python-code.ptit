import math

t = int(input())
for k in range(t):
    a = list(map(int, input()))
    s = sum(a)
    if s % 10:
        print("NO")
        continue
    else:
        kt = 1
        for i in range(1, len(a)):
            kt &= (abs(a[i] - a[i - 1]) == 2)
        print("YES" if kt else "NO")
