p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

dp = [[] for i in range(0, 51)]
for i in range(2, 51):
    if i in p:
        dp[i].append(-i)
        for j in dp[i - 1]:
            dp[i].append(j)
            if i * abs(j) <= 1e18:
                dp[i].append(-i * j)
    else:
        dp[i] = dp[i - 1]

while True:
    s = input()
    if s.split()[0] == '-1':
        break
    l, r = map(int, s.split())
    n = int(input())
    cnt_l = cnt_r = 0
    for i in dp[n]:
        cnt_r += int(r / i)
        cnt_l += int((l - 1) / i)
    print(r - l + 1 - (cnt_l - cnt_r))
