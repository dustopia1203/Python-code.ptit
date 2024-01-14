s = input()
cnt = int(input())
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
a.sort()
check = False
for i in a:
    if d[i] >= cnt:
        print(i, d[i])
        check = True
if not check:
    print("NOT FOUND")
