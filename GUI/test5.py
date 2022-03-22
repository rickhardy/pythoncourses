# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:53:26 2022

@author: rmh_r
"""

from guizero import App, PushButton, Box, Text


def change():
    if b1.bg == 'green':
        b1.bg = 'yellow'
    else:
        b1.bg = 'green'


def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        # reset the timer
        timer.cancel(counter)
        app.warn("Uh oh!", "You are almost out of biscuits!")
 
def time_out():
    app.warn("Uh oh!", "You are almost out of biscuits!")
    timer.cancel (timer)
    timer.value = 'game over'
 
  
        
app = App("textsize")

extra_features = Box(app)
timer = Text(extra_features, text="Get Ready")
timer.value = 30
timer.repeat(100, counter)


b1 = PushButton(app, text="bigger")
b1.repeat(1000, change)

app.display()