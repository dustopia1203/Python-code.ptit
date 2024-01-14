for _ in range(int(input())):
    a = input()
    ans = "YES"
    for i in range(len(a) - 1):
        if int(a[i]) > int(a[i + 1]):
            ans = "NO"
            break
    print(ans)
