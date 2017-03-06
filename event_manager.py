__author__ = 'robert'


class EventManager:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener):
        "prihlasi posluchaca"
        self.listeners[listener] = 1

    def unregister_listener(self, listener):
        "zrusi posluchaca, ten sa zrusi sam, ak nanho zaniknu vsetky referencie"
        if listener in self.listeners:
            del self.listeners[listener]

    def post(self, event):
        for listener in self.listeners:
            listener.notify(event)