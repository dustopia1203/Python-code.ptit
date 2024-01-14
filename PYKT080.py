d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

n, m = map(int, input().split())
a = []
q = []
for i in range(n):
    a.append([int(i) for i in input().split()])
    for j in range(m):
        if a[i][j] == -1:
            q.append([i, j])
ans = 0
while len(q) != 0:
    front = q.pop(0)
    i = front[0]
    j = front[1]
    for k in d:
        x = i + k[0]
        y = j + k[1]
        if 0 <= x < n and 0 <= y < n:
            ans += a[x][y]
            a[x][y] = 0
print(ans)
