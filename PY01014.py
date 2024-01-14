check = False
a, k, n = map(int, input().split())
b = k - a % k
while a + b <= n:
    print(b, end=" ")
    check = True
    b += k
if not check:
    print("-1")
else:
    print()
