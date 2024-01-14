a = []
n = int(input())
for _ in range(n):
    c = input()
    if a.count(c) == 0:
        a.append(c)
print(len(a))
