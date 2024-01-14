class Student:
    def __init__(self, id, name, cls):
        self.id = id
        self.name = name
        self.cls = cls
        self.cc = 10

    def calc(self, s):
        for i in s:
            if i == 'm':
                self.cc -= 1
            elif i == 'v':
                self.cc -= 2
        if self.cc < 0:
            self.cc = 0

    def __str__(self):
        s = "" if self.cc > 0 else "KDDK"
        return f"{self.id} {self.name} {self.cls} {self.cc} {s}"


n = int(input())
a = []
for i in range(n):
    a.append(Student(input(), input(), input()))
for i in range(n):
    s = input().split()
    for j in a:
        if j.id == s[0]:
            j.calc(s[1])
for i in a:
    print(i)
