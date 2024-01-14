def check(n):
    return str(n) == str(n)[::-1] and len(str(n)) > 1


n, m = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(n)]
M = -1
for i in range(n):
    for j in range(m):
        if check(a[i][j]) and a[i][j] > M:
            M = a[i][j]
if M == -1:
    print("NOT FOUND")
else:
    print(M)
    for i in range(n):
        for j in range(m):
            if a[i][j] == M:
                print(f"Vi tri [{i}][{j}]")
