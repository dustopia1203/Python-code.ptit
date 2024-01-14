import math

prime = [1] * 501
prime[0] = prime[1] = 0
for i in range(2, int(math.sqrt(501)) + 1):
    if prime[i]:
        for j in range(i * i, 501, i):
            prime[j] = 0


for _ in range(int(input())):
    n = input()
    cnt_prime = 0
    for i in n:
        if prime[int(i)] == 1:
            cnt_prime += 1
    print("YES" if cnt_prime > len(n) - cnt_prime and prime[len(n)] == 1 else "NO")
