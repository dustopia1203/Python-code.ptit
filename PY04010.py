class Student:
    def __init__(self, name, dob, p1, p2, p3):
        self.name = name
        self.dob = dob
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.tp = p1 + p2 + p3

    def __str__(self):
        res = f"{self.name} {self.dob} {self.tp:.1f}"
        return res


a = Student(input(), input(), float(input()), float(input()), float(input()))
print(a)
