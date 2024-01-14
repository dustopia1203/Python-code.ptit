n = 0
d = ['2', '3', '5', '7']
res = []


def check(s):
    if s[-1] == '2':
        return False
    ck = [0] * 4
    for i in s:
        for j in range(4):
            if i == d[j]:
                ck[j] = 1
    return sum(ck) == 4


n = int(input())
