def cnt(s, d):
    if s == 'Xe_con':
        if d == '5':
            return 10000
        else:
            return 15000
    if s == 'Xe_tai':
        return 20000
    if s == 'Xe_khach':
        if d == '29':
            return 50000
        else:
            return 70000


n = int(input())
m = {}
for i in range(n):
    a = input().split()
    if a[3] == 'IN':
        if a[4] not in m:
            m[a[4]] = cnt(a[1], a[2])
        else:
            m[a[4]] += cnt(a[1], a[2])
m = sorted(m.items(), key=lambda x: x[0])
for i in m:
    print(str(i[0]) + ':', i[1])
