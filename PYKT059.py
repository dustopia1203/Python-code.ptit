used = [[] for i in range(300)]
a = [[] for i in range(300)]


def dfs(u):
    used[u] = 1
    for i in a[u]:
        if not used[i]:
            dfs(i)


n, m, u = map(int, input().split())
for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
dfs(u)
for i in range(1, n + 1):
    if not used[i]:
        print(i)
