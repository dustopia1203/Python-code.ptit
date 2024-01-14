import math

digit = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}
t = int(input())
while t > 0:
    b = int(input())
    s = input()
    n = int(math.log(b, 2))
    while len(s) % n != 0:
        s = "0" + s
    i = 0
    while i < len(s):
        tmp = 0
        for j in range(i, i + n):
            tmp += int(s[j]) * (2 ** (n - j + i - 1))
        print(digit[tmp], end="")
        i += n
    t -= 1
    print()
