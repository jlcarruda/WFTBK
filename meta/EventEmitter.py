from WFTBK import *
from meta import *


class EventBroadcaster(object):
    __instance = None
    __eventstacks = {} # {"event1": [obj1, obj2, obj3]}

    def __new__(cls, *args, **kwargs): #SINGLETON PATTERN
        if not cls.__instance:
            cls.__instance = super(EventBroadcaster, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


    def subscribe(self, obj, event):

        if not self.__eventstacks.has_key(event):
            self.__eventstacks[event] = []

        self.__eventstacks[event].append(obj)

    def emit(self, stack, options=None):

        if self.__eventstacks.has_key(stack):
            obj = self.__eventstacks[stack]

            for subscriber in obj:
                subscriber()


def toDeckBuilderWin(self):

    if not gui.WindowHandler().isCreated("Deckbuilder"):
        win = gui.WindowHandler().createWindow("sprites/cleanBG.jpg", "Deckbuilder")
        virusDeck = GameObject.Button("sprites/VirusDeckSleeve.png", (230,200))
        antiVirusDeck = GameObject.Button("sprites/AntiVirusDeckSleeve.png", (450, 200))
        backButton = GameObject.Button("sprites/backButton.png")

        backButton.defineOnClickEvent(toMainMenuWin)
        virusDeck.defineOnClickEvent(toBattlefield)
        antiVirusDeck.defineOnClickEvent(toBattlefield)

        win.addGameObject(virusDeck)
        win.addGameObject(antiVirusDeck)
        win.addGameObject(backButton)

        print win.getGameObjects()
    else:
        win = gui.WindowHandler().getElement("Deckbuilder")
    GameLoop().changeWindow(win)

def toMainMenuWin(self):

    if not gui.WindowHandler().isCreated("MainMenu"):

        win = gui.WindowHandler().createWindow("sprites/main-menu-new.png", "MainMenu")

        startButton = meta.Button("sprites/start.png",  (300,330))
        tutorialButton = meta.Button("sprites/tutorial.png", (300,400))
        quitButton = meta.Button("sprites/quit.png", (300,470))

        startButton.defineOnClickEvent(meta.EventEmitter.toDeckBuilderWin)
        quitButton.defineOnClickEvent(quit)

        win.addGameObject(quitButton)
        win.addGameObject(startButton)
        win.addGameObject(tutorialButton)

    else:
        win = gui.WindowHandler().getElement("MainMenu")

    GameLoop().changeWindow(win)


def toBattlefield(self):

    if not gui.WindowHandler().isCreated("Battlefield"):
        win = gui.WindowHandler().createWindow("sprites/battlefield.jpg", "Battlefield")

    else:
        win = gui.WindowHandler().getElement("Battlefield")

    GameLoop().changeWindow(win)