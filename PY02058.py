n, m = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(n)]
c = -1
d = 10001
for i in a:
    c = max(max(i), c)
    d = min(min(i), d)
luck_num = c - d
check = False
for i in a:
    if luck_num in i:
        check = True
        break
if not check:
    print("NOT FOUND")
else:
    print(luck_num)
    for i in range(n):
        for j in range(m):
            if a[i][j] == luck_num:
                print(f"Vi tri [{i}][{j}]")
