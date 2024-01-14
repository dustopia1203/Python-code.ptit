n = int(input())
a = [float(i) for i in input().split()]
m = 11
M = 0
for i in a:
    m = min(m, i)
    M = max(M, i)
while m in a:
    a.remove(m)
while M in a:
    a.remove(M)
print(f"{sum(a) / len(a):.2f}")
