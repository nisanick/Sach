from event import VysledokEvent, PrekresliEvent, ClickEvent, PohniEvent, PrepocitaneEvent
from sachovnica import Sachovnica

__author__ = 'robert'


class Hra:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.sachovnica = Sachovnica(event_manager)
        self.klikol = False
        self.prva = None
        self.event_manager.post(PrekresliEvent(self.sachovnica.figurky))

    def notify(self, event):
        if isinstance(event, VysledokEvent):
            if event.podaril_sa:
                self.event_manager.post(PrekresliEvent(self.sachovnica.figurky))
        elif isinstance(event, PrepocitaneEvent):
            if self.klikol:
                self.klikol = False
                self.event_manager.post(PohniEvent(self.prva, self.zmen_na_suradnicu(event.x, event.y)))
                self.prva = None
            else:
                self.klikol = True
                self.prva = self.zmen_na_suradnicu(event.x, event.y)

    def zmen_na_suradnicu(self, z, na):
        return str(chr(z+64)) + str(na)