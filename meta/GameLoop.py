from WFTBK import *

def quit(self):
    GameLoop().shutdown()

class GameLoop(object):

    __instance = None

    __gameClock = None
    __eventBroadcaster = None
    __currentWindow = None
    __screen = pygame.display.get_surface()
    __windowHandler = None
    running = False

    def __call__(self, *args, **kwargs):
        return self.__instance

    def __new__(cls, *args, **kwargs): #SINGLETON PATTERN
        if not cls.__instance:
            cls.__gameClock = pygame.time.Clock()

            cls.__eventBroadcaster = meta.EventBroadcaster()
            cls.__windowHandler = gui.WindowHandler()
            cls.__currentWindow = cls.__windowHandler.createWindow("sprites/main-menu-new.png", "MainMenu")

            startButton = meta.Button("sprites/start.png",  (300,330))
            tutorialButton = meta.Button("sprites/tutorial.png", (300,400))
            quitButton = meta.Button("sprites/quit.png", (300,470))

            startButton.defineOnClickEvent(meta.EventEmitter.toDeckBuilderWin)
            quitButton.defineOnClickEvent(quit)

            print cls.__currentWindow
            cls.__currentWindow.addGameObject(quitButton)
            cls.__currentWindow.addGameObject(startButton)
            cls.__currentWindow.addGameObject(tutorialButton)
            cls.__instance = super(GameLoop, cls).__new__(cls, *args)
        return cls.__instance

    def initLoop(self):

        self.running = True
        while self.running:
            event = pygame.event.poll()
            if event.type == QUIT:
                sys.exit()

            # this is the injection of the handler of the window into the game loop, passing the event
            self.__currentWindow.windowScheduleFunction(event)

            pygame.display.flip()
            self.__gameClock.tick(FPS) # It will tame the game loop to run on 60 fps

    def changeWindow(self, window):
        print 'Window changed to ' + window.name

        # Add the window into the windowHandler if it wasn't added yet
        if not self.__windowHandler.getElement(window.name):
            self.__windowHandler.addElement(window)

        self.__currentWindow = window

    def setWindowHandler(self, handler):

        if self.__windowHandler == None:
            self.__windowHandler = handler

    def getWindowHandler(self):
        return self.__windowHandler

    def shutdown(self):
        self.running = False

