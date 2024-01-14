f = [1] * 10
for i in range(2, 10):
    f[i] = f[i - 1] * i


t = int(input())
for _ in range(t):
    n = int(input())
    tmp = str(n)
    cmp = 0
    for i in tmp:
        cmp += f[int(i)]
    if cmp == n:
        print("Yes")
    else:
        print("No")
