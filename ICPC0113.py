import math

prime = [1] * 1000005
prime[0] = prime[1] = 0
for i in range(2, int(math.sqrt(1000005))):
    if prime[i] == 1:
        for j in range(i * i, 1000005, i):
            prime[j] = 0

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(13, n, 2):
        if prime[i] == 1:
            tmp = str(i)
            tmp = tmp[::-1]
            if int(tmp) < n and tmp > str(i) and prime[int(tmp)] == 1:
                print(i, int(tmp), end=" ")
    print()
