import pygame
import sys
from event import PrekresliEvent, ClickEvent, PrepocitaneEvent

__author__ = 'robert'


class Grafika:

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        pygame.init()
        self.screen = pygame.display.set_mode((540, 540))
        self.screen.fill((255, 255, 255))

        self.pozadie_sachovnice = pygame.Surface((530, 530))
        self.pozadie_sachovnice.fill((0, 0, 0))

        self.cierne_policko = pygame.Surface((64, 64))
        self.cierne_policko.fill((130, 45, 0))
        #self.cierne_policko.fill((0, 0, 0))

        self.biele_policko = pygame.Surface((64, 64))
        self.biele_policko.fill((250, 220, 200))
        #self.biele_policko.fill((255, 255, 255))

        self.cierne_rect = []
        self.biele_rect = []
        #for y in range(7, -1, -1):
        for y in range(0, 8):
            for x in range(0, 8):
                if (x+y) % 2 == 1:
                    self.cierne_rect.append(pygame.Rect((x*66 + 7, y*66 + 7), (64, 64)))
                else:
                    self.biele_rect.append(pygame.Rect((x*66 + 7, y*66 + 7), (64, 64)))

        self.textura = pygame.image.load("textura.png")
        alpha = 175
        self.textura.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        self.figurky = pygame.image.load("sprite.png")

    def prekresli(self, figurky):
        self.screen.blit(self.pozadie_sachovnice, pygame.Rect((5, 5), (530, 530)))
        for rect in self.cierne_rect:
            self.screen.blit(self.cierne_policko, rect)
        for rect in self.biele_rect:
            self.screen.blit(self.biele_policko, rect)
        self.screen.blit(self.textura, pygame.Rect((5, 5), (530, 530)))

        for figurka in figurky:
            self.screen.blit(self.figurky, ((figurka.x - 1)*66 +7, 462 - (figurka.y - 1)*66 +7), pygame.Rect(figurka.sprite, (64, 64)))
        pygame.display.flip()

    def notify(self, event):
        if isinstance(event, PrekresliEvent):
            self.prekresli(event.figurky)
