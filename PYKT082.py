def trans(x):
    if 3 <= x <= 4:
        return 2.5
    if 5 <= x <= 6:
        return 3.0
    if 7 <= x <= 9:
        return 3.5
    if 10 <= x <= 12:
        return 4.0
    if 13 <= x <= 15:
        return 4.5
    if 16 <= x <= 19:
        return 5.0
    if 20 <= x <= 22:
        return 5.5
    if 23 <= x <= 26: 
        return 6.0
    if 27 <= x <= 29:
        return 6.5
    if 30 <= x <= 32:
        return 7.0
    if 33 <= x <= 34:
        return 7.5
    if 35 <= x <= 36:
        return 8.0
    if 37 <= x <= 38:
        return 8.5
    if 39 <= x <= 40:
        return 9.0


t = int(input())
for i in range(t):
    a = input().split()
    r, l = int(a[0]), int(a[1])
    s, w = float(a[2]), float(a[3])
    x = (trans(r) + trans(l) + s + w) / 4.0
    if x - int(x) >= 0.75:
        print(int(x) + 1.0)
    elif x - int(x) >= 0.25:
        print(int(x) + 0.5)
    else:
        print(int(x))
