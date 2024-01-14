def Try(l, s="", a=0, b=0, c=0):
    if len(s) == l:
        if 0 < a <= b <= c:
            print(s)
        return
    Try(l, s + 'A', a + 1, b, c)
    Try(l, s + 'B', a, b + 1, c)
    Try(l, s + 'C', a, b, c + 1)


n = int(input())
for i in range(3, n + 1):
    Try(i)
