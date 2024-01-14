import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = input()
    print("YES" if isPrime(int(n[0:3])) and isPrime(int(n[-3:])) else "NO")
    