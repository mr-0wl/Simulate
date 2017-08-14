# Simulate is a Simon clone
# From Invent with Python
#A learning thing for working into game development
# No copyright

import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500 #IN MS
FLASHDELAY = 200 #IN MS
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 #seconds before gameover if no button pressed

# RGB
WHITE = (255, 255, 255)
BRIGHTRED = (255, 0, 0)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
BRIGHTGREEN = (0, 255, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
DARKGRAY = (40, 40, 40)
bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE / 2)
              
#Rect objects for each 4 buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
              
def main():
              
