# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 19:13:38 2022

@author: rmh_r
"""

from guizero import App, Text

def game_over():
    timer.value = "Game Over"

def timer_tick():
    timer.time_left = timer.time_left - 1 
    if timer.time_left <=0:
        game_over()
    else:
        timer.value = timer.time_left /10

app = App("Quiz question app")
timer = Text(app, text = "Get Ready")
timer.time_left = 100
timer.repeat(100,timer_tick)

app.display()
