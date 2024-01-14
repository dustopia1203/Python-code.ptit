for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(0, n - 2):
        left = i + 1
        right = n - 1
        x = a[i]
        while left < right:
            if x + a[left] + a[right] == 0:
                ans += 1
                left += 1
            elif x + a[left] + a[right] < 0:
                left += 1
            else:
                right -= 1
    print(ans)
