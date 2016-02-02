from WFTBK import *

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
        self.loadedSprite = pygame.image.load(self.sprite)

        if onClickEvent != None:
            self.onClick = types.MethodType(onClickEvent, self)

    def tick(self):

        e = pygame.event.poll()
        if e.type == MOUSEBUTTONDOWN and self.__isClicked():
            print "Clicou!"
            if self.onClick != None and type(self.onClick).__name__ == "instancemethod":
                self.onClick()
                return

    def render(self):
        # Render the sprites into the window in the position
        return (self.loadedSprite, self.pos)

    def __isClicked(self): #return boolean
        mouseX, mouseY = pygame.mouse.get_pos() #tuple
        x, y = self.pos
        w, h = self.loadedSprite.get_size()
        varX = x + w
        varY = y + h

        if mouseX > x and mouseX < varX and mouseY > y and mouseY < varY:
            return True
        return False

    def defineOnClick(self, function):
        self.onClick = types.MethodType(function, self)
