#!/bin/python
#-----------------------------------------------------------------------------
# File Name : rdk.py
# Author: Emre Neftci
#
# Creation Date : Wed 27 Mar 2019 05:13:06 PM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2
#----------------------------------------------------------------------------- 
import random
import numpy as np
import time
import psychopy.visual
import psychopy.event
import sys
clock = psychopy.core.Clock()
win = psychopy.visual.Window(
    size=[800, 800],
    units="pix",
    fullscr=False
)

n_dots = 200

dot_xys = []
np.random.seed(int(time.time()))
d = np.random.choice([0,180])

for dot in range(n_dots):

    dot_x = random.uniform(-200, 200)
    dot_y = random.uniform(-200, 200)

    dot_xys.append([dot_x, dot_y])

dot_stim = psychopy.visual.DotStim(
    win=win,
    fieldSize=(800.0, 800.0),
    coherence = float(sys.argv[1]),
    dir=d,
    dotSize=5.0,
    nDots=n_dots
)

while clock.getTime() < 2.5:
    dot_stim.draw()
    win.flip()

psychopy.event.waitKeys()

win.close()

print('Direction was {0}'.format(d))
