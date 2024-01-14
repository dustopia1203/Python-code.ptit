ans = []


def Try(i, n, res, sum=0):
    if sum > n:
        return
    if sum == n:
        ans.append(res)
        return
    for j in range(i, 0, -1):
        Try(j, n, res + [j], sum + j)

    
for _ in range(int(input())):
    n = int(input())
    res = []
    Try(n, n, res)
    print(len(ans))
    for i in ans:
        print("(", end='')
        print(*i, end='')
        print(")", end=' ')
    print()
    ans = []
