# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# guizero - Hero name generator
from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox, ListBox, CheckBox, Picture
import time


def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.value = "You are... The " + hero + "."
    
def dark_mode():
    if checkbox.value == 0:
        app.bg = 'Green'
        checkbox.text_color = "Yellow"
    else:
        app.bg = 'Red'
        checkbox.text_color = "White"
           



app = App(title="Hero-o-matic", height=600, width=800)
app.bg = 'Red'

# Function definitions for your events go here.

# Your GUI widgets go here
message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Enter a colour?")
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal")
cmb_animal = Combo(app, options=["Aardvark", "Cat", "Dolphin", "Tiger", "Velociraptor", "Walrus","Dog",], selected="Aardvark", width=20)

btn_make_name = PushButton(app, text='Make me a hero', command=make_hero_name)
lbl_output = Text(app, text="A hero name will appear here")


listbox = ListBox(app, items=["Beef", "Chicken", "Fish", "Vegetarian"])

checkbox = CheckBox (app, text="Dark Mode")
checkbox.toggle()
checkbox.update_command (dark_mode)

picture = Picture(app, image="dragon1.png", grid = [100,10], width=100, height=100)

app.display()


# Set up event triggers here

# Show the GUI on the screen, start listening to events.



