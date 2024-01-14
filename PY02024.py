def mul_digit(n):
    res = 1
    for i in n:
        res *= int(i)
    return res


for t in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=lambda s: (mul_digit(s), int(s)))
    print(*a)
