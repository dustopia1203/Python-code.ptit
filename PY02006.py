for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    check = True
    for i in range(n):
        if a[i] > b[i]:
            check = False
            break
    print("YES" if check else "NO")
