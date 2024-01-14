n = int(input())
m = {}
for i in range(n - 1):
    x, y = map(int, input().split())
    if m.get(x) is None:
        m[x] = 1
    else:
        m[x] += 1
    if m.get(y) is None:
        m[y] = 1
    else:
        m[y] += 1
check = True
cnt = 0
for i in m.keys():
    if m[i] > 1:
        cnt += 1
    if cnt > 1:
        check = False
        break
print("Yes" if check else "No")
