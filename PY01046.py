def hanoi(n, src, des, tmp):
    if n == 1:
        print(f"{src} -> {des}")
    else:
        hanoi(n - 1, src, tmp, des)
        print(f"{src} -> {des}")
        hanoi(n - 1, tmp, des, src)


n = int(input())
hanoi(n, 'A', 'C', 'B')
