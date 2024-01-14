def checkSoLuong(s):
    cntU = 0
    cntL = 0
    for i in s:
        if (i.islower()):
            cntL += 1
    cntU = len(s) - cntL
    return cntL >= cntU


s = input()
if (checkSoLuong(s)):
    print(s.lower())
else:
    print(s.upper())
