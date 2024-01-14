import string


a = string.ascii_uppercase
d = {}
for i in range(len(a)):
    d[a[i]] = i

for _ in range(int(input())):
    s = input()
    n = int(len(s) / 2)
    s1 = s[:n]
    s2 = s[n:]
    r_val1 = 0
    r_val2 = 0
    for i in range(n):
        r_val1 += d[s1[i]]
        r_val2 += d[s2[i]]
    r_string1 = ""
    r_string2 = ""
    for i in range(n):
        r_string1 += a[(d[s1[i]] + r_val1) % 26]
        r_string2 += a[(d[s2[i]] + r_val2) % 26]
    m_string = ""
    for i in range(n):
        m_string += a[(d[r_string1[i]] + d[r_string2[i]]) % 26]
    print(m_string)
