__author__ = 'robert'


class Jazdec:
    def __init__(self, x, farba):
        self.pohyby = 0
        self.farba = farba
        self.x = x
        if farba == 1:
            self.sprite = (128, 0)
            self.y = 1
            self.symbol = 'N'
        else:
            self.sprite = (128, 64)
            self.y = 8
            self.symbol = 'n'

    def posun_sa(self, x, y):
        self.x = x
        self.y = y
        self.pohyby += 1

    def je_tah_povoleny(self, x, y):
        if x < 1 or y < 1 or x > 8 or y > 8:
            return False
        if x == self.x and y == self.y:
            return False

        if (abs(self.x - x) == 1 and abs(self.y - y) == 2) or (abs(self.x - x) == 2 and abs(self.y - y) == 1):
            return True
        return False