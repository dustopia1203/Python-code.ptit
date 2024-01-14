for _ in range(int(input())):
    n = int(input())
    m = {}
    a = [int(i) for i in input().split()]
    for i in a:
        if m.get(i) is None:
            m[i] = 1
        else:
            m[i] += 1
    for i in m.keys():
        if m[i] % 2 == 1:
            print(i)
            break
