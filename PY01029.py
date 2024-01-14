import math

for _ in range(int(input())):
    n = input()
    rev = n[::-1]
    n, rev = int(n), int(rev)
    if math.gcd(n, rev) == 1:
        print("YES")
    else:
        print("NO")
