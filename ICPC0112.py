import math

prime = [1] * 1000005
prime[0] = prime[1] = 0
for i in range(2, int(math.sqrt(1000005))):
    if prime[i] == 1:
        for j in range(i * i, 1000005, i):
            prime[j] = 0

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    cnt = 0
    for i in range(3, n - 5, 2):
        if prime[i] == 1 and prime[i + 2] == 1 and prime[i + 6] == 1:
            cnt += 1
        elif prime[i] == 1 and prime[i + 4] == 1 and prime[i + 6] == 1:
            cnt += 1
    print(cnt)
