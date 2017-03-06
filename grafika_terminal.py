from event import PrekresliEvent

__author__ = 'robert'


class GrafikaTerminal:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    def notify(self, event):
        if isinstance(event, PrekresliEvent):
            self.vykresli(event.figurky)

    def vykresli(self, figurky):
        for y in range(8, 0, -1):
            if y == 8:
                print("  _A__B__C__D__E__F__G__H_")
            print(y, end="|")
            for x in range(1, 9):
                for figurka in figurky:
                    if figurka.x == x and figurka.y == y:
                        symbol = figurka.symbol
                        break
                else:
                    if(x + y) % 2 == 0:
                        symbol = " "
                    else:
                        symbol = "#"
                if(x + y) % 2 == 0:
                    print(" " + symbol + " ", end="")
                else:
                    print("#" + symbol + "#", end="")
            print("|", y, sep="")
            if y == 1:
                char = str(u"\u203E")
                print("  " + char + "A" + 2*char + "B" + 2*char + "C" + 2*char + "D" + 2*char + "E" + 2*char + "F" + 2*char + "G" + 2*char + "H" + char)
        print()