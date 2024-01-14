for _ in range(int(input())):
    n = input()
    tichChan = 1
    tongLe = 0
    check = False
    for i in range(0, len(n), 2):
        if n[i] != '0':
            tichChan *= int(n[i])
            check = True
    for i in range(1, len(n), 2):
        tongLe += int(n[i])
    if not check:
        tichChan = 0
    print(tichChan, tongLe)
