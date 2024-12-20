# window.py
"""
title: Class for pygame window
author: Laksh Chopra
date-created: 19/03/24
"""

import pygame

class Window:
    """
    Creates the window that will host the cv2 frame
    """

    def __init__(self, TITLE, WIDTH=800, HEIGHT=600, FPS=30):
        self.__TITLE = TITLE
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIMENSIONS)
        self.__SURFACE.fill((40, 40, 40))
        pygame.display.set_caption(self.__TITLE)

    ### --- MODIFIER METHODS --- ###
    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.__SURFACE.fill((40, 40, 40))

    ### --- ACCESSOR METHODS --- ###
    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT

