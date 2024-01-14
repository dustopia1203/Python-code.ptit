from itertools import *

s = input()
a = [c for c in s]
per = list(permutations(a))
for i in per:
    for j in i:
        print(j, end="")
    print()
