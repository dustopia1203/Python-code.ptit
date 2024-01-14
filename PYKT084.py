cnt = 0
title = ""
d = {}
for _ in range(int(input())):
    s = input()
    if s == "":
        cnt = 0
    else:
        if cnt == 0:
            title = s
            d[title] = 0
        else:
            d[title] = cnt
        cnt += 1
for i in d.keys():
    print(f"{i}: {d[i]}")
