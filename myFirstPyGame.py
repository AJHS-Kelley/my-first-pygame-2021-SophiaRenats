# My First PyGame, Sophia Rentas, 12/1/21 2:21, v0.13

import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup our window. 1
windowSurface = pygame.display.set_mode((500, 400),0, 32)
pygame.display.set_caption('Hello, world')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE= (0, 0, 255)
VELVET = (128, 10, 41)

#Setup font.
basicFont = pygame.font.SysFont(None,48)

#Setup text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill background color
windowSurface.fill(VELVET)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, WHITE, ((146,0), (291,106), (236,277), (56,277), (0,106)))

# Draw lines on the screen.
pygame.draw.line(windowSurface, BLUE, (60,60),(120,60), 4)
pygame.draw.line(windowSurface, GREEN, (50,40),(100,40), 6)
pygame.draw.line(windowSurface, RED, (236,82),(236,82), 9)

# Draw a circle.
pygame.draw.circle(windowSurface, BLACK, (300,50), 20,0)

# Draw and ellipse.
pygame.draw.ellipse(windowSurface, RED, (300,250,40,80), 1)

# Draw the text rectangle.
pygame.draw.rect(windowSurface, GREEN, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Create Pixel Array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLUE
del pixArray

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

# Update PyGame Display
pygame.display.update()

# Run game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()