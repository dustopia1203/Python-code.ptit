for _ in range(int(input())):
    n = input()
    d = 0
    for i in n:
        d += int(i)
    d = str(d)
    print("YES" if len(d) > 1 and d == d[::-1] else "NO")
