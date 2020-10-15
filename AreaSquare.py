class Square:
    def __init__(self, a):
        if a > 0:
            self._a = a

    @property
    def AreaSquare(self):
        return self._a ** 2

    @AreaSquare.setter
    def AreaSquare(self, value):
        if value >= 0:
            self._a = value
        else:
            raise ValueError("a must be >= 0")

a = int(input())
Rec = Square(a)
Rec.AreaSquare = a
print(Rec.AreaSquare)
