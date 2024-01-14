while True:
    a = [int(i) for i in input().split()]
    if a[0] == a[1] == a[2] == a[3] == 0:
        break
    cnt = 0
    while True:
        if a[0] == a[1] == a[2] == a[3]:
            break
        cnt += 1
        tmp = a[0]
        for i in range(0, 3):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - tmp)
    print(cnt)
