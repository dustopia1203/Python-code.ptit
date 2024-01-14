import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    s = input()
    n = int(s[-4::])
    print("YES" if isPrime(n) else "NO")
