s1 = input().lower().split()
s2 = input().lower().split()
union = sorted(set(s1 + s2))
inter = sorted(set(s1).intersection(set(s2)))
for i in union:
    print(i, end=' ')
print()
for i in inter:
    print(i, end=' ')
print()
