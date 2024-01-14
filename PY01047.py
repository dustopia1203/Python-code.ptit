prime = [1] * 10001
prime[0] = prime[1] = 0
for i in range(2, 101):
    if prime[i] == 1:
        for j in range(i * i, 10001, i):
            prime[j] = 0
for _ in range(int(input())):
    n = int(input()[-4:])
    print("YES" if prime[n] == 1 else "NO")
