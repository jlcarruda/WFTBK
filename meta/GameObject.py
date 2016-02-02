from WFTBK import *

class __GameObject(object):
    sprite = None #Path of image loaded by pygame
    loadedSprite = None
    pos = None
    def __init__(self, sprite, pos=(0,0)):
        self.sprite = sprite
        self.pos = pos

    def tick(self, event):
        pass

    def render(self):
        pass

    def onInputFocus(self):
        pass

    def onInputBlur(self):
        pass

    def onClick(self):
        pass

    def onMouseOver(self):
        pass

    # Binder Functions
    def defineOnClickEvent(self, function):
        self.onClick = types.MethodType(function, self)

    def defineOnMouseOverEvent(self, function):
        self.onMouseOver = types.MethodType(function, self)

    def defineOnInputFocus(self, function):
        self.onInputFocus = types.MethodType(function, self)

    def defineOnInputBlur(self, function):
        self.onInputBlur = types.MethodType(function, self)

    def __containsPoint(self, mousePos):
        mouseX, mouseY = mousePos #tuple
        x, y = self.pos
        w, h = self.loadedSprite.get_width(), self.loadedSprite.get_height()
        varX = x + w
        varY = y + h

        if mouseX > x and mouseX < varX and mouseY > y and mouseY < varY:
            return True
        return False


class Button(__GameObject):

    __eventAssociated = None

    def __init__(self, sprite, pos=(0,0)): # sprite = Obj, pos = tuple
        super(Button, self).__init__(sprite, pos)
        self.sprite = sprite
        self.loadedSprite = pygame.image.load(self.sprite)

    def tick(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == LEFTMOUSEBUTTON:
            if self.__containsPoint(event.dict['pos']):
                self.onClick()

    def render(self):
        # Render the sprites into the window in the position
        return (self.loadedSprite, self.pos)