# Simple Animation with PyGame, Sophia Rentas, 1/5/22, 2:07, v0.1

import pygame, sys, time
from pygame.locals import *

# Setup PyGame 
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
