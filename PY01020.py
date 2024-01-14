for _ in range(int(input())):
    s = input()
    i = len(s)
    if s[i - 1] == '6' and s[i - 2] == '8':
        print("YES")
    else:
        print("NO")
