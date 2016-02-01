import WFTBK

class Window():
    background = None
    __loadedBackground = None
    __gameObjects = []
    __eventHandler = None
    name = None

    # Here will have all the stuff that needs to be updated/rendered/checked in every run of the gameLoop
    def windowScheduleFunction(self, gameLoop):
        self.tick()
        self.render()

    def addGameObject(self, object):
        self.__gameObjects.append(object)

    def removeGameObject(self, object):
        self.__gameObjects.pop(object)

    def tick(self):
        for object in self.__gameObjects:
            object.tick()

    #The render of all objects of the window. Including the background and the game objects
    def render(self):
        if self.__loadedBackground == None:
            self.__loadedBackground = WFTBK.pygame.image.load(self.background).convert_alpha()

        # It will blit the background of the screen first
        WFTBK.Session.screen.blit(self.__loadedBackground, (0,0))

        for object in self.__gameObjects:
            sprite, pos = object.render()
            WFTBK.Session.screen.blit(sprite, pos)

        # Draw the back buffer into the front buffer
        WFTBK.pygame.display.flip()

    def getMousePos(self):

        return WFTBK.pygame.mouse.get_pos()

    def setGameObjects(self, listObjects):
        if type(listObjects).__name__ == "list":
            for element in listObjects:
                if type(element).__name__ != "instance":
                    return
        self.__gameObjects = listObjects

    def getGameObjects(self):
        print self
        return self.__gameObjects
