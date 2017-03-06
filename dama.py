__author__ = 'robert'


class Dama:
    def __init__(self, farba):
        self.pohyby = 0
        self.farba = farba
        self.x = 4
        if farba == 1:
            self.sprite = (256, 0)
            self.y = 1
            self.symbol = 'Q'
        else:
            self.sprite = (256, 64)
            self.y = 8
            self.symbol = 'q'

    def posun_sa(self, x, y):
        self.x = x
        self.y = y
        self.pohyby += 1

    def je_tah_povoleny(self, x, y):
        if x < 1 or y < 1 or x > 8 or y > 8:
            return False
        if x == self.x and y == self.y:
            return False

        if self.x == x or self.y == y:
            return True

        if abs(self.x - x) == abs(self.y - y):
            return True
        return False