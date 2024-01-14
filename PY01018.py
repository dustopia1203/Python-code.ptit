P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s = input()
    if s[0] == '0':
        break
    k, n = s.split()
    k = int(k)
    n = n[::-1]
    for i in n:
        idx = P.find(i)
        print(P[(idx + k) % 28], end="")
    print()
