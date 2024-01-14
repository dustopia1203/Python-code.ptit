import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rdc(self):
        tmp = math.gcd(self.x, self.y)
        self.x /= tmp
        self.y /= tmp

    def __str__(self):
        return "%d/%d" % (self.x, self.y)


x, y = map(int, input().split())
p = Point(x, y)
p.rdc()
print(p)
