for _ in range(int(input())):
    n = input()
    tongChan = 0
    tichLe = 1
    check = False
    for i in range(0, len(n), 2):
        tongChan += int(n[i])
    for i in range(1, len(n), 2):
        if n[i] != '0':
            tichLe *= int(n[i])
            check = True
    if not check:
        tichLe = 0
    print(tongChan, tichLe)
