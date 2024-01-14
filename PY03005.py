import re
from collections import Counter

n, k = map(int, input().split())
s = ""
for i in range(n):
    s += input() + " "
a = re.findall("\\w+", s.lower())
a.sort()
m = sorted(Counter(a).items(), key=lambda i: i[1], reverse=True)
for key, value in m:
    if value < k:
        break
    print(key, value)
