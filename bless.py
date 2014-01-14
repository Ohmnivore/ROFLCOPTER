# -*- coding: utf-8 -*-
import time
import os
import colorama
from colorama import init, Fore, Back, Style
from random import choice
from random import randint
import platform

if (platform.system() is 'Windows'):
    init(autoreset=True)

copter = """
| ROFL:ROFL:R        |
|         _^___      |
|      __/   [] \    |
|LOL===__        \   |
|        \________]  |
|         I   I      |
|        --------/   |
"""
#copter2 = open(os.path.join(os.path.dirname(__file__), "roflcopter",
                           #"copter2.txt")).read()

copter2 = """
|         L:ROFL:ROFL|
|         _^___      |
| L    __/   [] \    |
| O ===__        \   |
| L      \________]  |
|         I   I      |
|        --------/   |
"""

pos = lambda y, x: '\x1b[%d;%dH' % (y, x)
MINY, MAXY = 1, 24
MINX, MAXX = 1, 80

FORES = [Fore.RED, Fore.GREEN, Fore.YELLOW,
        Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW,
        Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
STYLES = [Style.DIM, Style.NORMAL, Style.BRIGHT]

FORE = 0
STYLE = Style.NORMAL
BACK = 0
SUBCOUNT = 0

frame = True


def InitAll():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


InitAll()

while (True):
    time.sleep(0.1)
    if (frame is True):
        print(pos(MINY, MINX) + FORES[FORE] + STYLE + BACKS[BACK] + copter)
        frame = False
    else:
        print(pos(MINY, MINX) + FORES[FORE] + STYLE + BACKS[BACK] + copter2)
        frame = True
    SUBCOUNT += 1
    if (SUBCOUNT >= 30):
        SUBCOUNT = 0
        FORE = randint(0, len(FORES) - 1)
        STYLE = choice(STYLES)
        BACK = randint(0, len(BACKS) - 1)
        if (BACK is not 0):
            while (BACK is FORE + 1):
                BACK = randint(0, len(BACKS) - 1)