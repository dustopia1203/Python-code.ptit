for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    m = min(a)
    M = max(a)
    cnt = 0
    for i in range(m, M + 1):
        if not i in a:
            cnt += 1
    print(cnt)
