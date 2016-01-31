import pygame
from Window import *
from pygame.locals import *
from ScreenOne import ScreenOne
from meta.GameObject import Button
from gui.WindowHandler import WindowHandler

class MainMenu(Window):
    background = "sprites/main-menu.png"
    name = 'MainMenu'
    __gameObjects = [Button('sprites/quit.png', (100,100))]

    def windowScheduleFunction(self, gameLoop, event = None):
        super(MainMenu, self).windowScheduleFunction(gameLoop)

        for e in pygame.event.get():
            if e.type == "TEST":
                print 'hey'
            if e.type == MOUSEBUTTONDOWN:
                print 'pressed'

    def verifyClickButton(self, posMouse):
        x, y = posMouse #tuple
        startButtonImg = pygame.image.load('sprites/start.png').convert_alpha()
        tutorialButtonImg = pygame.image.load('sprites/tutorial.png').convert_alpha()
        quitButtonImg = pygame.image.load('sprites/quit.png').convert_alpha()

        startButton = (304,352)
        tutorialButton = (304, 423)
        quitButton = (282, 496)

        buttons = { 'start': startButtonImg, 'tutorial':tutorialButtonImg, 'quit': quitButtonImg}

        for b, k in buttons.iteritems():
            w, h = k.get_size()

            vX = x + w
            vY = y + h

            print b
            if b == 'start':
                if startButton[0] > x and x < vX and y > startButton[1] and y < vY:
                    return b

                else:
                    return False
            if b == 'tutorial':
                if tutorialButton[0] > x and x < vX and y > tutorialButton[1] and y < vY:
                    return b
                else:
                    return False
            if b == 'quit':
                if quitButton[0] > x and x < vX and y > quitButton[1] and y < vY:
                    return b
                else:
                    return False

