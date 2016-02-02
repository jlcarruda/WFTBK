from WFTBK import *

class EventBroadcaster(object):
    __instance = None
    __eventstacks = {} # {"event1": [obj1, obj2, obj3]}

    def __new__(cls, *args, **kwargs): #SINGLETON PATTERN
        if not cls.__instance:
            cls.__instance = super(EventBroadcaster, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


    def subscribe(self, obj, event):

        if not self.__eventstacks.has_key(event):
            self.__eventstacks[event] = []

        self.__eventstacks[event].append(obj)

    def emit(self, stack, options=None):

        if self.__eventstacks.has_key(stack):
            obj = self.__eventstacks[stack]

            for subscriber in obj:
                subscriber()
