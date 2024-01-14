st = []
for _ in range(int(input())):
    ans = []
    s = input()
    cnt = 1
    for i in s:
        if i == '(':
            st.append(cnt)
            ans.append(cnt)
            cnt += 1
        elif i == ')':
            ans.append(st.pop())
    print(*ans)
