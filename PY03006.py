import re
from collections import Counter

n = int(input())
s = ""
for i in range(n):
    s += input() + " "
a = re.findall("[a-z|A-Z]+", s.lower())
a.sort()
m = sorted(Counter(a).items(), key=lambda i: i[1], reverse=True)
for key, value in m:
    print(key, value)
