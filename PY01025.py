s = input()
n = len(s) - 1
tmp = ""
d = []
cnt = 0
while n >= 0:
    tmp = s[n] + tmp
    n -= 1
    cnt += 1
    if cnt == 3:
        d.append(tmp)
        tmp = ""
        cnt = 0
if tmp != "":
    d.append(tmp)

d.reverse()
for i in range(len(d) - 1):
    print(d[i] + ",", end="")
print(d[len(d) - 1])
