n, k = map(int, input().split())
s = set(map(int, input().split()))
a = sorted(list(s))
res = []
n = len(a)


def Try(i):
    if len(res) == k:
        for i in res:
            print(i, end=" ")
        print()
    for j in range(i, n):
        res.append(a[j])
        Try(j + 1)
        res.pop()


Try(0)
