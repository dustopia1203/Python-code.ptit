for _ in range(int(input())):
    s = input()
    for i in range(0, len(s) - 1, 2):
        for __ in range(int(s[i + 1])):
            print(s[i], end="")
    print()
