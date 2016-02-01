import WFTBK

from Window import Window
class ScreenOne(Window):
    background = 'sprites/screen-bg.png'
    __gameObjects = []
    name = 'ScreenOne'

    def windowScheduleFunction(self, gameLoop, event = None):
        super(ScreenOne, self).windowScheduleFunction(gameLoop)

        for e in WFTBK.pygame.event.get():
            if e.type == WFTBK.MOUSEBUTTONDOWN:
                nextWindow = gameLoop.getWindowHandler().getElement('MainMenu')
                gameLoop.changeWindow(nextWindow)
