def check(n, k, u, v, g):
    q = [u]
    a = [0] * (n + 1)
    a[u] = 1
    while len(q) > 0:
        x = q.pop()
        if x == v:
            return False
        for i in g[x]:
            if i != k and a[i] == 0:
                q.append(i)
                a[i] = 1
    return True


for _ in range(int(input())):
    n, m, u, v = map(int, input().split())
    g = [[] for i in range(n + 1)]
    for i in range(m):
        s = input().split()
        x = int(s[0])
        y = int(s[1])
        g[x].append(y)
    res = 0
    for i in range(1, n + 1):
        if i != u and i != v:
            if check(n, i, u, v, g):
                res += 1
    print(res)
