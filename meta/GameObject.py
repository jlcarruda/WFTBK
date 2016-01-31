import pygame
import random
pygame.display.init()
#Abstract
class __GameObject(object):
    __sprite = None #Path of image loaded by pygame
    __loadedSprite = None
    __pos = None
    def __init__(self, sprite, pos=(0,0), eventType="BUTTONPRESSED"):
        self.__sprite = sprite
        self.__pos = pos

    def tick(self):
        pass

    def render(self):
        pass

class Button(__GameObject):

    __eventAssociated = None

    def __init__(self, sprite, pos=(0,0), eventType=None): # sprite = Obj, pos = tuple
        super(Button, self).__init__(sprite, pos)
        if(eventType == None):
            eventType = random.randint(0,99999)
        self.__sprite = sprite
        self.__eventAssociated = pygame.event.Event(eventType, {"obj": self})

        pygame.event.post(self.__eventAssociated)

    def tick(self):
        # See if the button is clicked
        # Do something
        pass

    def render(self):
        # Render the sprites into the window in the position
        #TODO: Need to finish the logic
        #TODO: Fix the bug that says that pygame is no initialized
        if self.__loadedSprite == None:
            self.__loadedSprite = pygame.image.load(self.__sprite)

        return (self.__loadedSprite, self.__pos)