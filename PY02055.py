import math


def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


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
