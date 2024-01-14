s = input()
res = ""
while len(s) % 3 != 0:
    s = '0' + s
for i in range(0, len(s), 3):
    n = int(s[i:i + 3], 2)
    res = res + str(n)
print(res)
