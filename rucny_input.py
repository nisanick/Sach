from event import TickEvent, PrepocitaneEvent, QuitEvent

__author__ = 'robert'


class RucnyInput:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.inputy = [(1, 2), (1, 4), (1, 1), (1, 3)] #do tohto zoznamu treba vpisat inputy, ak nemame modul pygame

    def notify(self, event):
        if isinstance(event, TickEvent):

            for event in self.inputy:
                ev = PrepocitaneEvent(event[0], event[1])

                self.event_manager.post(ev)
            self.event_manager.post(QuitEvent())