def recover(b, n):
    a = []
    for i in range(0, n):
        a.append(1)
    if n == 2:
        return a

    sum_b = 0
    for i in range(0, n):
        sum_b += sum(b[i])
    sum_a = (sum_b / 2) / (n - 1)
    a[0] = int((sum(b[0]) - sum_a) / (n - 2))
    for i in range(1, n):
        a[i] = b[0][i] - a[0]
    return a


n = int(input())
b = []
for i in range(0, n):
    b.append([int(i) for i in input().split()])
print(*recover(b, n))
