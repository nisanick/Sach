__author__ = 'robert'


class TickEvent:
    pass


class QuitEvent:
    pass


class ClickEvent:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PrepocitaneEvent:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PohniEvent:
    def __init__(self, odkial, kam):
        self.odkial = odkial
        self.kam = kam


class VysledokEvent:
    def __init__(self, podaril_sa):
        self.podaril_sa = podaril_sa


class PrekresliEvent:
    def __init__(self, figurky):
        self.figurky = figurky