a = []
n = int(input())
while len(a) != n:
    tmp = [int(i) for i in input().split()]
    a.extend(tmp)
M = max(a)
ans = []
for i in range(1, M):
    if i not in a:
        ans.append(i)
if len(ans) == 0:
    print("Excellent!")
else:
    for i in ans:
        print(i)
