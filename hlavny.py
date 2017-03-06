import importlib

from event_manager import EventManager
import imp
from game_loop import GameLoop
from grafika import Grafika
from grafika_terminal import GrafikaTerminal
from hra import Hra
from input import InputController
from rucny_input import RucnyInput

__author__ = 'hudec29'


event_manager = EventManager()

'''try:
    importlib.find_loader('pygame')
    importlib.find_loader('Grafika')
	grafika = Grafika(event_manager)
    vstup = InputController(event_manager)
except:
    grafika = GrafikaTerminal(event_manager)
    vstup = RucnyInput(event_manager)'''
	

#grafika = Grafika(event_manager)
gr2 = GrafikaTerminal(event_manager)
#vstup = InputController(event_manager)
vs2 = RucnyInput(event_manager)

hra = Hra(event_manager)
loop = GameLoop(event_manager)

loop.run()