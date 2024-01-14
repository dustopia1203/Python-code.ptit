prime = [1] * 10001
prime[0] = prime[1] = 0
for i in range(2, 101):
    if prime[i] == 1:
        for j in range(i * i, 10001, i):
            prime[j] = 0
for _ in range(int(input())):
    n = input()
    s = 0
    for i in n:
        s += int(i)
    print("YES" if prime[s] == 1 else "NO")
