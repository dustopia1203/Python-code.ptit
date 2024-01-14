s = input()
a = []
i = 0
while i < len(s) - 1:
    n = int(s[i:i + 2])
    if n not in a:
        a.append(n)
    i += 2
for i in a:
    print(i, end=' ')
