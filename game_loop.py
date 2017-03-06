from event import TickEvent, QuitEvent

__author__ = 'robert'

class GameLoop:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.bez = True

    def run(self):
        "hlavny cyklus hry"
        while self.bez:
            event = TickEvent()
            self.event_manager.post(event)

    def notify(self, event):
        "prijatie eventu pre ukoncenie programu"
        if isinstance(event, QuitEvent):
            self.bez = False