res = []
for _ in range(int(input())):
    s = input()
    if len(s) < 100:
        res.append(s)
    else:
        i = 99
        while s[i] != ' ':
            i -= 1
        s = s[:i + 1]
        res.append(s)
for i in res:
    print(i)
