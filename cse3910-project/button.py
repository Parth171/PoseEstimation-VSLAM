"""
Title: Button Class
"""


import pygame

class Button():


    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0,COLOR=(255, 255, 255)):
        self._SURFACE = pygame.Surface

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.X = X
        self.Y = Y
        self.POS = (self.X, self.Y)
        self._DIM = (self.WIDTH, self.HEIGHT)
        self.COLOR = COLOR
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self.COLOR)



    # --- MODIFIER --- #


    def setX(self, X):
        self.X = X
        self.POS = (self.X, self.Y)

    def setY(self, Y):
        self.Y = Y
        self.POS = (self.X, self.Y)

    def setPOS(self, X, Y):
        self.setX(X)
        self.setY(Y)

    def setColor(self, TUPLE):
        self.COLOR = TUPLE

    def getSurface(self):
        return self._SURFACE

    def getPOS(self):
        return self.POS

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

if __name__ == "__main__":

    from window import Window
    pygame.init()

    WINDOW = Window("Boxes subclass")

    RED_BOX = Button(100, 100)
    RED_BOX.setColor((255, 0, 0))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(RED_BOX.getSurface(), RED_BOX.getPOS())
        WINDOW.updateFrame()