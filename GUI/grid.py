# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:55:56 2022

@author: rmh_r
"""

from guizero import App, Text, Box

app = App()

box = Box(app,layout="grid", width="fill", height="fill")

red = Text(box, bg="red", grid=[0,0])
blue = Text(box, bg="blue", grid=[0,1])
green = Text(box, bg="green", grid=[1,0])
white = Text(box, bg="white", grid=[1,1])

app.display()