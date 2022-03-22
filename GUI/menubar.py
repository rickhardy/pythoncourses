# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:00:47 2022

@author: rmh_r
"""

from guizero import App, TextBox, PushButton, Box, Combo, CheckBox, Slider, MenuBar


def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()

def save_file(param1):
    print (param1)
    with open(file_name.value, "w") as f:
        f.write(editor.value)
        save_button.disable()

def enable_save():
    save_button.enable()

# A new function that closes the app
def exit_app():
    app.destroy()
    
def add_monkeys(num_monkeys):
    #print (type(num_monkeys))
    for monkeys in range(0,  num_monkeys):
        editor.value += 'Monkey '
    editor.focus()

def edit_function():
    print("Edit option")


# This is where any additional functions needed to run your script go

app = App(title="textzero")

# The new MenuBar
menubar = MenuBar(app,
                  # These are the menu options
                  toplevel=["Monkeys", "Elephants"],
                  # The options are recorded in a nested lists, one list for each menu option
                  # Each option is a list containing a name and a function
                  options=[
                      [ ["Add Monkey", lambda:add_monkeys(1)], ["Two monkeys",lambda:add_monkeys(2)] ],
                      [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]
                  ])


file_controls = Box(app, align="top", width="fill", border=True)
file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left")

save_button = PushButton(file_controls, text="Save", command=lambda:save_file("Saving File"), align="right")
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

editor = TextBox(app, multiline=True, height="fill", width="fill", command=enable_save)

# This is where your additional features go

app.display()
