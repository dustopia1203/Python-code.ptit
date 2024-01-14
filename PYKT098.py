limit = 2 ** 31 - 1
a = []
with open("DATA.in", 'r') as file:
    for line in file.readlines():
        for i in line.split():
            try:
                n = int(i)
                if n > limit:
                    a.append(i)
            except Exception:
                a.append(i)
a.sort()
print(*a)
