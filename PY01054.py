for _ in range(int(input())):
    n = input()
    m = 1
    for i in n:
        if i != '0':
            m *= int(i)
    print(m)
