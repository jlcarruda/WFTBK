import pygame, os, math, sys

import gui
from config.default import *
import gui
from meta.EventEmitter import *
from meta.GameLoop import *
from gui import *
from pygame.locals import *
from time import sleep

screen = pygame.display.set_mode(resolution, 0, 32)
pygame.init()

class Session(object):

    __instance = None

    #__windowHandler = WindowHandler()

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
        mainMenu = MainMenu() # Main Window
        windowHandler.addElement(mainMenu)

        loop = GameLoop(mainMenu, screen, self.__EventBroadcaster)
        loop.setWindowHandler(windowHandler)

        loop.initLoop()


if __name__== "__main__":
    Session = Session()
    Session()
