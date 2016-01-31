import WFTBK
from WFTBK import *
# Needs to initialize the display to use it

#Abstract
class __GameObject(object):
    sprite = None #Path of image loaded by pygame
    loadedSprite = None
    pos = None
    def __init__(self, sprite, pos=(0,0)):
        self.sprite = sprite
        self.pos = pos

    def tick(self):
        pass

    def render(self):
        pass

class Button(__GameObject):

    __eventAssociated = None
    onClick = None

    def __init__(self, sprite, onClickEvent=None,pos=(0,0)): # sprite = Obj, pos = tuple
        super(Button, self).__init__(sprite, pos)
        self.sprite = sprite

        print onClickEvent
        self.onClick = WFTBK.types.MethodType(onClickEvent, self)

    def tick(self):
        # See if the button is clicked
        # Do something
        if self.loadedSprite == None:
            self.loadedSprite = pygame.image.load(self.sprite)

        for e in WFTBK.pygame.event.get():
            if e.type == MOUSEBUTTONDOWN and self.__isClicked():
                if self.onClick != None and type(self.onClick).__name__ == "instancemethod":
                    self.onClick()

    def render(self):
        # Render the sprites into the window in the position
        return (self.loadedSprite, self.pos)

    def __isClicked(self): #return boolean
        mouseX, mouseY = WFTBK.pygame.mouse.get_pos() #tuple
        x, y = self.pos
        w, h = self.loadedSprite.get_size()

        varX = x + w
        varY = y + h

        if mouseX > x and mouseX < varX and mouseY > y and mouseY < varY:
            return True
        return False

    def defineOnClick(self, function):
        self.onClick = WFTBK.types.MethodType(function, self)
