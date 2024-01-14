n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = set(a)
s2 = set(b)
check = True
for i in s1:
    if i not in s2:
        check = False
        break
print("YES" if check else "NO")
