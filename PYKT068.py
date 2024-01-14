class MonHoc:
    def __init__(self, ma, ten, ht):
        self.ma = ma
        self.ten = ten
        self.ht = ht

    def __str__(self):
        return self.ma + " " + self.ten + " " + self.ht


a = []
for _ in range(int(input())):
    a.append(MonHoc(input(), input(), input()))
a.sort(key=lambda i: i.ma)
for i in a:
    print(i)
