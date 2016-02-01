from WFTBK import *
from Window import Window
class MainMenu(Window):
    background = "sprites/main-menu.png"
    name = 'MainMenu'
    __gameObjects = []

    def windowScheduleFunction(self, gameLoop, event = None):
        super(MainMenu, self).windowScheduleFunction(gameLoop)

    def tick(self):
        pass