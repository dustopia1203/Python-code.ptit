a = input()
cnt4 = cnt7 = 0
for i in a:
    if int(i) == 4:
        cnt4 += 1
    if int(i) == 7:
        cnt7 += 1
if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7:
    print("YES")
else:
    print("NO")
