n = int(input())
while n > 0:
    cnt = 1
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
    print(cnt)
    n = int(input())
