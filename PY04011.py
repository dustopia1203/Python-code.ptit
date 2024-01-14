d = set()
ck = {}
bbv = {}
q = []
for _ in range(int(input())):
    a = [i for i in input().split()]
    if a[1] == '<':
        tmp = a[0]
        a[0] = a[2]
        a[2] = tmp
    if ck.get(a[0]) is None:
        ck[a[0]] = [a[2]]
    else:
        ck[a[0]].append(a[2])
    if bbv.get(a[2]) is None:
        bbv[a[2]] = 1
    else:
        bbv[a[2]] += 1
    d.add(a[0])
    d.add(a[2])
for i in d:
    if bbv.get(i) is None:
        q.append(i)
cnt = 0
while len(q) != 0:
    tmp = q.pop(0)
    cnt += 1
    if not ck.get(tmp) is None:
        for i in ck[tmp]:
            bbv[i] -= 1
            if bbv[i] == 0:
                q.append(i)
print("possible" if cnt == len(d) else "impossible")
