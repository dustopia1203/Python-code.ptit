prime = [1] * 501
prime[0] = prime[1] = 0
for i in range(2, 23):
    if prime[i] == 1:
        for j in range(i * i, 501, i):
            prime[j] = 0


def check(n):
    if prime[len(n)] == 0:
        return False
    cnt_p = 0
    for i in n:
        cnt_p += prime[int(i)]
    if cnt_p <= len(n) - cnt_p:
        return False
    return True


for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")
