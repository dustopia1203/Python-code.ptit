n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = set()
s2 = set()
s3 = set()
for i in a:
    if i in b:
        s1.add(i)
    else:
        s2.add(i)   
for i in b:
    if i not in s1:
        s3.add(i)
for i in sorted(s1):
    print(i, end=' ')
print()
for i in sorted(s2):
    print(i, end=' ')
print()
for i in sorted(s3):
    print(i, end=' ')
print()
