__author__ = 'robert'


class Veza:

    def __init__(self, x, farba):
        self.pohyby = 0
        self.farba = farba
        self.x = x
        if farba == 1:
            self.sprite = (192, 0)
            self.y = 1
            self.symbol = 'R'
        else:
            self.sprite = (192, 64)
            self.y = 8
            self.symbol = 'r'

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
        return False