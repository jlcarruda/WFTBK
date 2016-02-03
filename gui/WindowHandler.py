from gui import Window

class WindowHandler(object):
    __elements = {}
    __instance = None

    def __call__(self, *args, **kwargs):
        return self.__instance

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(WindowHandler, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def addElement(self, element):
        try:
            self.__elements[element.name] = element
        except:
            print 'Error in trying to assign element ' + element

    def getElement(self, name):
        return self.__elements[name]

    def removeElement(self, name):
        self.__elements.pop(name)
        return

    def createWindow(self, background, name):
        window = Window()
        window.name = name
        window.background = background
        self.addElement(window)
        return window


