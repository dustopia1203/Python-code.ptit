s = input()
a = []
i = 0
while i < len(s) - 1:
    n = int(s[i:i + 2])
    a.append(n)
    i += 2
a = sorted(set(a))
for i in a:
    print(i, end=' ')
