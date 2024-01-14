for _ in range(int(input())):
    n = input()
    rev_n = n[::-1]
    check = True
    for i in range(0, len(n) - 1):
        if abs(ord(n[i]) - ord(n[i + 1])) != abs(ord(rev_n[i]) - ord(rev_n[i + 1])):
            check = False
            break
    print("YES" if check else "NO")
