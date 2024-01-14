for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n % 7 != 0:
        cnt += 1
        n += int(str(n)[::-1])
        if cnt == 1000:
            break
    print(n)
