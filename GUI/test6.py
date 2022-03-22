# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:16:32 2022

@author: rmh_r
"""

from guizero import App
app = App(title="Biscuit monitor")
app.warn("Uh oh!", "You are almost out of biscuits!")
app.display()