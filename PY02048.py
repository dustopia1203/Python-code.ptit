n, k = map(int, input().split())
a = sorted([int(i) for i in input().split()])
cnt = 1
for i in range(len(a) - 1):
    if a[i + 1] - a[i] > k:
        cnt += 1
print(cnt)
