for _ in range(int(input())):
    n = int(input())
    a = []
    while n:
        a.append([int(i) for i in input().split()])
        n -= 1
    a.sort(key=lambda x: (x[1], x[0]))
    ans = 0
    curr = -1
    for i in a:
        if curr <= i[0]:
            curr = i[1]
            ans += 1
    print(ans)
