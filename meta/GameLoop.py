import WFTBK

class GameLoop(object):

    __instance = None

    __eventBroadcaster = None
    __currentWindow = None
    __screen = None
    __windowHandler = None

    def __init__(self, initialWindow=None, eventBroadcaster=None ):
       # self.__windowHandler = windowHandler
        self.__eventBroadcaster = eventBroadcaster
        self.__currentWindow = initialWindow

    def __new__(cls, *args, **kwargs): #SINGLETON PATTERN
        if not cls.__instance:
            cls.__instance = super(GameLoop, cls).__new__(cls, *args)
        return cls.__instance

    def initLoop(self):

        while True:
            if WFTBK.pygame.event.peek(WFTBK.QUIT):
                exit()
                break
            # this is the injection of the handler of the window into the game loop
            self.__currentWindow.windowScheduleFunction(self)

    def changeWindow(self, window):
        print 'Window changed to ' + window.name

        # Add the window into the windowHandler if it wasn't added yet
        if not self.__windowHandler.getElements().has_key(window.name):
            self.__windowHandler.addElement(window)

        self.__currentWindow = window

    def setWindowHandler(self, handler):

        if self.__windowHandler == None:
            self.__windowHandler = handler

    def getWindowHandler(self):
        return self.__windowHandler