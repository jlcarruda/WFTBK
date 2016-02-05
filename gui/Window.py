import pygame

class Window():
    background = None
    __loadedBackground = None
    __gameObjects = None
    __eventHandler = None
    name = None

    # Here will have all the stuff that needs to be updated/rendered/checked in every run of the gameLoop
    def windowScheduleFunction(self, event):
        self.tick(event)
        self.render()

    def addGameObject(self, object):
        if self.__gameObjects == None:
            self.__gameObjects = []
        self.__gameObjects.append(object)

    def removeGameObject(self, object):
        if self.__gameObjects == None:
            self.__gameObjects = []

        self.__gameObjects.pop(object)

    def tick(self, event):
        if self.__gameObjects == None:
            self.__gameObjects = []

        for object in self.__gameObjects:
            object.tick(event)

    #The render of all objects of the window. Including the background and the game objects
    def render(self):
        if self.__loadedBackground == None:
            self.__loadedBackground = pygame.image.load(self.background).convert_alpha()

        # It will blit the background of the screen first
        pygame.display.get_surface().blit(self.__loadedBackground, (0,0))

        for object in self.__gameObjects:
            sprite, pos = object.render()
            pygame.display.get_surface().blit(sprite, pos)

    def getMousePos(self):
        return pygame.mouse.get_pos()
