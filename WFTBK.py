import pygame
from pygame.locals import *
import random
from gui import *
from meta import *
from config import *
import types

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
        windowHandler = WindowHandler()
        loop = GameLoop()
        loop.setWindowHandler(windowHandler)

        def onClickStartButton(self):
            nextWindow = windowHandler.getElement('test')
            loop.changeWindow(nextWindow)

        def onClickQuitButton(self):
            sys.exit()

        startButton = Button("sprites/start.png", onClickStartButton, (300,300))
        tutorialButton = Button("sprites/tutorial.png", None, (300,200))
        quitButton = Button("sprites/quit.png", onClickQuitButton, (300,100))

        mainMenu = windowHandler.createWindow("sprites/main-menu.png", "MainMenu")
        mainMenu.addGameObject(startButton)
        mainMenu.addGameObject(tutorialButton)
        mainMenu.addGameObject(quitButton)
        testWindow = windowHandler.createWindow("sprites/screen-bg.png", "test")

        print mainMenu.addGameObject
        print testWindow.addGameObject
        loop.changeWindow(mainMenu)

        loop.initLoop()

if __name__== "__main__":
    Session = Session()
    Session()
