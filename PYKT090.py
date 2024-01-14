a = set()
with open("CONTACT.in", 'r') as file:
    for i in file.readlines():
        if i.endswith('\n'):
            i = i[:-1]
        a.add(i.lower())
a = list(sorted(a))
for i in a:
    print(i)
