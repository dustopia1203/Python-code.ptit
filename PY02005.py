def merge_sort(a, l, r):
    cnt = 0
    if l < r:
        m = (l + r) // 2
        cnt += merge_sort(a, l, m)
        cnt += merge_sort(a, m + 1, r)
        cnt += merge(a, l, m, r)
    return cnt


def merge(a, l, m, r):
    cnt = 0
    a1 = a[l:m + 1]
    a2 = a[m + 1:r + 1]
    i = j = 0
    k = l
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            cnt += len(a1) - i
            j += 1
            k += 1
    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1
    return cnt


n = int(input())
a = [int(i) for i in input().split()]
print(merge_sort(a, 0, n - 1))
