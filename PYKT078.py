for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    M = max(a)
    i = -1
    for j in range(n):
        if a[j] == M:
            i = j
            break
    a.insert(i, m)
    for j in a:
        if j < 0:
            print(j, end=' ')
    for j in a:
        if j >= 0:
            print(j, end=' ')
    print()