for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    m = {}
    M = [0, 0]
    for i in a:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
        if m[i] > M[1]:
            M = [i, m[i]]
    if M[1] <= n/2:
        print("NO")
    else:
        print(M[0])
