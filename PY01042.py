char = ['0', '1', '2']


def check(s):
    for i in s:
        if not i in char:
            return False
    return True


for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
