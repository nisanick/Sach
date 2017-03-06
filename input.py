import pygame
from pygame.locals import *
from event import TickEvent, QuitEvent, ClickEvent, PrepocitaneEvent

__author__ = 'robert'

LEFT = 1


class InputController:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    def notify(self, event):
        if isinstance(event, TickEvent):

            for event in pygame.event.get():
                ev = None
                if event.type == QUIT:
                    ev = QuitEvent()
                elif event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                    ev = ClickEvent(event.pos[0], event.pos[1])

                self.event_manager.post(ev)
        elif isinstance(event, ClickEvent):
            x,y = self.prepocitaj(event.x, event.y)
            self.event_manager.post(PrepocitaneEvent(x,y))

    def prepocitaj(self, x, y):
        suradnica_x = x//66 + 1
        suradnica_y = 8 - y//66
        return (suradnica_x, suradnica_y)