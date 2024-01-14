base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def convert(n, b):
    a = []
    while n > 0:
        a.append(n % b)
        n //= b
    s = ""
    a.reverse()
    for i in a:
        s += base[int(i)]
    return s


for _ in range(int(input())):
    n, b = map(int, input().split())
    print(convert(n, b))
