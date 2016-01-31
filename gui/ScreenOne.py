import pygame
from Window import *
from pygame.locals import *
from gui.WindowHandler import WindowHandler


class ScreenOne(Window):
    background = 'sprites/screen-bg.png'
    name = 'ScreenOne'

    def windowScheduleFunction(self, gameLoop, event = None):
        super(ScreenOne, self).windowScheduleFunction(gameLoop)

        for e in pygame.event.get():
            if e.type == MOUSEBUTTONDOWN:
                nextWindow = gameLoop.getWindowHandler().getElement('MainMenu')
                gameLoop.changeWindow(nextWindow)
