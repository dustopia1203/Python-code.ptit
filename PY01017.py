t = int(input())
for k in range(t):
    s = input()
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]: j += 1
        if j != i:
            print(str(j - i) + s[i], end="")
            i = j
        else:
            print("1" + s[i], end="")
            i += 1
    print()
