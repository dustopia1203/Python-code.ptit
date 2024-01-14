import math

t = int(input())
for k in range(t):
    n = int(input())
    print("1 * ", end="")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d = 0
            while n % i == 0:
                d += 1
                n //= i
            print(str(i) + "^" + str(d), end="")
            if n != 1:
                print(" * ", end="")
            else:
                print()
    if n > 1:
        print(str(n) + "^" + str(1))
