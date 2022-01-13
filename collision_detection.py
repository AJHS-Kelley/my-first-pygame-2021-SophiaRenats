# PyGame Collision Detection Practice, Sophia Rentas, January 13, 2022, 10:24am, v0.2

import pygame, sys, random
from pygame.locals import

# Setup PyGame
pygame.init()
mainClock = pygame.time.Clock()

# Setup the PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.disply.set_model((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption ('Collision Detection 2022')