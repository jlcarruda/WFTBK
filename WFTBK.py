import pygame
from pygame.locals import *
import random
from gui import *
from meta import *
from config import *
import types

def onClickStartButton(self):
    #nextWindow = windowHandler.getElement('test')
    #gameLoop.changeWindow(nextWindow)
    print "hey"

class Session(object):
    screen = pygame.display.set_mode(resolution, 0, 32)
    __instance = None

    __spritesRootPath = 'sprites'
    __EventBroadcaster = EventBroadcaster()

    def __new__(cls, *args, **kwargs): #SINGLETON PATTERN
        if not cls.__instance:
            cls.__instance = super(Session, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __call__(self, *args, **kwargs):
        self.__startSession()

    def getEventBroadcaster(self):
        return self.__EventBroadcaster

    def __startSession(self):
        self.__importDependencies()
        windowHandler = WindowHandler()
        loop = GameLoop()
        loop.setWindowHandler(windowHandler)

        testWindow = windowHandler.createWindow("sprites/screen-bg.png", "test")

        button = Button("sprites/start.png", onClickStartButton, (300,300))

        #button.onClick = types.MethodType(onClickStartButton, button)
        print button.onClick()

        mainMenu = windowHandler.createWindow("sprites/main-menu.png", "MainMenu")
        mainMenu.addGameObject(button)
        loop.changeWindow(mainMenu)

        loop.initLoop()

    def __importDependencies(self):
        import pygame



if __name__== "__main__":
    Session = Session()
    Session()
