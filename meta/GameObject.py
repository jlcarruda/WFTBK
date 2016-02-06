from WFTBK import *

class __GameObject(object):
    sprite = None # Path of image loaded by pygame
    loadedSprite = None
    pos = None

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

    def onMouseMove(self):
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

    def defineOnMouseMove(self, function):
        self.onMouseMove = types.MethodType(function, self)

    def containsPoint(self, mousePos):
        mouseX , mouseY = mousePos #tuple
        x, y = self.pos
        w, h = self.loadedSprite.get_width(), self.loadedSprite.get_height()
        varX = x + w
        varY = y + h

        if mouseX > x and mouseX < varX and mouseY > y and mouseY < varY:
            return True
        return False


class Button(__GameObject):

    def __init__(self, sprite, pos=(0,0)): # sprite = Obj, pos = tuple
        self.sprite = sprite
        self.pos = pos
        self.loadedSprite = pygame.image.load(self.sprite)

    def tick(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == LEFTMOUSEBUTTON:
            if self.containsPoint(event.dict['pos']):
                self.onClick()

    def render(self):
        # Render the sprites into the window in the position
        return (self.loadedSprite, self.pos)


class Card(__GameObject):
    __backSprite = None
    __frontSprite = None
    __isFlipped = True

    def __init__(self, frontSprite, backSprite = None, pos=(0,0)):
        self.__backSprite = pygame.image.load(backSprite).convert_alpha()
        self.__frontSprite = pygame.image.load(frontSprite).convert_alpha()
        self.pos = pos

    def tick(self, event):
        pass

    def render(self):
        if self.__isFlipped:
            return (self.__frontSprite, self.pos)
        return (self.__backSprite, self.pos)

    def changePos(self, pos):
        self.pos = pos

    def flip(self):
        self.__isFlipped = not self.__isFlipped

