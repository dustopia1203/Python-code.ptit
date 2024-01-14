class CuaRo:
    def __init__(self, name, donvi, tg):
        self.id = ""
        for i in donvi.split():
            self.id += i[0].upper()
        for i in name.split():
            self.id += i[0].upper()
        self.name = name
        self.donvi = donvi
        tgh = float(tg.split(':')[0]) - 6 + float(tg.split(':')[1]) / 60
        self.vantoc = 120 / tgh

    def __str__(self):
        return f"{self.id} {self.name} {self.donvi} {round(self.vantoc)} Km/h"


a = []
for _ in range(int(input())):
    a.append(CuaRo(input(), input(), input()))
a.sort(key=lambda i: i.vantoc, reverse=True)
for i in a:
    print(i)
