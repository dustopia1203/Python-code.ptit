def check(s):
    return s == s[::-1]


a = []
d = {}
M = -1
with open("VANBAN.in", 'r') as file:
    for lines in file.readlines():
        for i in lines.split():
            if i.endswith('\n'):
                i = i[:-1]
            if check(i):
                M = max(M, len(i))
                if i not in a:
                    a.append(i)
                if d.get(i) is None:
                    d[i] = 1
                else:
                    d[i] += 1
for i in a:
    if len(i) == M:
        print(i, d[i])
