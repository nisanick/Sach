__author__ = 'hudec29'




class Pesiak:

    def __init__(self, x, farba):
        self.pohyby = 0
        self.x = x
        self.farba = farba
        if farba == 2:
            self.sprite = (0, 64)
            self.symbol = 'p'
            self.y = 7
        else:
            self.sprite = (0, 0)
            self.symbol = 'P'
            self.y = 2

    def posun_sa(self, x, y):
        self.x = x
        self.y = y
        self.pohyby += 1

    def je_tah_povoleny(self, x, y):
        if x < 1 or y < 1 or x > 8 or y > 8:
            return False

        if x != self.x:
            return False

        if self.farba == 1:
            if self.y == 2 and y - self.y == 2:
                return True

            if y - self.y == 1:
                return True
        else:
            if self.y == 7 and self.y - y == 2:
                return True

            if self.y - y == 1:
                return True

    def mozem_vyhodit(self, x, y):
        if x < 1 or y < 1 or x > 8 or y > 8:
            return False

        if x == self.x and y == self.y:
            return False

        if abs(self.x - x) == 1:
            if self.farba == 1:
                if y - self.y == 1:
                    return True
            else:
                if self.y - y == 1:
                    return True
        return False