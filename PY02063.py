n = int(input())
a = [int(i) for i in input().split()]
a.sort()
c = a[-1] * a[-2] * a[-3]
d = a[0] * a[1] * a[-1]
e = a[-1] * a[-2]
f = a[0] * a[1]
res = max(max(max(c, d), e), f)
print(res)
