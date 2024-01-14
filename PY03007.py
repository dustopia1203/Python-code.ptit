import re

s = ""
pattern = "[\w\s,:]+"
while True:
    try:
        s += input()
    except Exception:
        break
a = re.findall(pattern, s)
for i in a:
    x = i.lower().split()
    x[0] = x[0].title()
    print(' '.join(x))
