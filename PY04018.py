subject = {'A': "TOAN", 'B': "LY", 'C': "HOA"}
prior = {'1': 2.0, '2': 1.5, '3': 1, '4': 0}


class Teacher:
    def __init__(self, name, id, cp, mp, num):
        self.name = name
        self.id = id
        self.cp = float(cp)
        self.mp = float(mp)
        self.tp = self.cp * 2 + self.mp + prior[id[1]]
        self.subj = subject[id[0]]
        self.idf = f"GV{num:02d}"
        self.check = "TRUNG TUYEN" if self.tp >= 18 else "LOAI"

    def __str__(self):
        return f"{self.idf} {self.name} {self.subj} {self.tp:.1f} {self.check}"


a = []
for _ in range(int(input())):
    a.append(Teacher(input(), input(), input(), input(), _ + 1))
a.sort(key=lambda i: i.tp, reverse=True)
for i in a:
    print(i)
