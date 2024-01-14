s = input()
a = []
d = {}
i = 0
while i < len(s) - 1:
    n = int(s[i:i + 2])
    if n not in a:
        a.append(n)
        d[n] = 1
    else:
        d[n] += 1
    i += 2
for i in a:
    print(i, d[i])
