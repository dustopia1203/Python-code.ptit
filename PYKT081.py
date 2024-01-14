for _ in range(int(input())):
    s = [i for i in input().split(".")]
    check = True
    if len(s) < 4:
        check = False
    for i in s:
        if i.isdigit():
            if int(i) > 255 or int(i) < 0:
                check = False
        else:
            check = False
    print("YES" if check else "NO")
