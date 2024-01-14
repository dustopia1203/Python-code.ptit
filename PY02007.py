b = set()
cnt = 0
while cnt < 10:
    a = [int(i) for i in input().split()]
    cnt += len(a)
    for i in a:
        b.add(i % 42)
print(len(b))
