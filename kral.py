__author__ = 'robert'


class Kral:
    def __init__(self, farba):
        self.pohyby = 0
        self.farba = farba
        self.x = 5
        if farba == 1:
            self.sprite = (320, 0)
            self.y = 1
            self.symbol = 'K'
        else:
            self.sprite = (320, 64)
            self.y = 8
            self.symbol = 'k'

    def posun_sa(self, x, y):
        self.x = x
        self.y = y
        self.pohyby += 1

    def je_tah_povoleny(self, x, y):
        if x < 1 or y < 1 or x > 8 or y > 8:
            return False
        if x == self.x and y == self.y:
            return False

        if (self.x == x and abs(self.y - y) == 1)or (self.y == y and abs(self.x - x) == 1):
            return True

        if abs(self.x - x) == abs(self.y - y) == 1:
            return True