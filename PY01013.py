import math

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
for _ in range(int(input())):
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    ans = 0
    while c > 0:
        ans += c % 10
        c //= 10
    if ans in prime:
        print("YES")
    else:
        print("NO")
