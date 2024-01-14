for _ in range(int(input())):
    n = input()
    s = 0
    for i in n:
        s += int(i)
    print("YES" if s % 3 == 0 else "NO")
