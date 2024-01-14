s = input()
while len(s) > 1:
    n = int(len(s) / 2)
    a = int(s[0:n])
    b = int(s[n:])
    s = str(a + b)
    print(s)
