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
