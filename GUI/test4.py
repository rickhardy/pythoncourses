# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:39:33 2022

@author: rmh_r
"""

from guizero import App, Text
from time import sleep

def countdown(t):
    while t > 0:
        t -= 1
        sleep(.01)
        print (t//60,':', t % 60)

countdown(120)
print ('Game Over')

#app.display()


