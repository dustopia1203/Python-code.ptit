n = int(input())
while n > 0:
    res = 10 ** 19
    s = input()
    s += "*"
    length = len(s)
    x = 0
    for i in range(0, length - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = min(res, x)
                x = 0
    print(res)
    n -= 1
