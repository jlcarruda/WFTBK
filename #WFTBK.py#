import meta
import gui
from config.default import *
import pygame, sys
import types
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(resolution, 0, 32)

class Session(object):
    __instance = None
    __spritesRootPath = 'sprites'

    def __new__(cls, *args, **kwargs): #SINGLETON PATTERN
        if not cls.__instance:
            cls.__instance = super(Session, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __call__(self, *args, **kwargs):
        self.__startSession()

    def __startSession(self):

        loop = meta.GameLoop()
        loop.initLoop()

if __name__== "__main__":
    Session = Session()
    Session()
