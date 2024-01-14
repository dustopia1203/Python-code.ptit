n = int(input())
while n > 0:
    s = input()
    s += "*"
    res = -1
    x = 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if not s[i + 1].isdigit():
                res = max(res, x)
                x = 0
    print(res)
    n -= 1
