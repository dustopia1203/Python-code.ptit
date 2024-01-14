import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rdc(self):
        tmp = math.gcd(self.x, self.y)
        self.x /= tmp
        self.y /= tmp

    def add(self, o):
        res_x = self.x * o.y + self.y * o.x
        res_y = self.y * o.y
        return Point(res_x, res_y)

    def __str__(self):
        return "%d/%d" % (self.x, self.y)


a, b, c, d = map(int, input().split())
p1 = Point(a, b)
p2 = Point(c, d)
res = p1.add(p2)
res.rdc()
print(res)
