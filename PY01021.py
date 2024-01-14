for _ in range(int(input())):
    s = input()
    a = []
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
        else:
            a.append(i)
    a.sort()
    for i in a:
        print(i, end='')
    print(sum)
