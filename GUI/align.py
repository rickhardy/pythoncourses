# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 18:08:55 2022

@author: rmh_r
"""


from guizero import App, TextBox, PushButton, Box, Combo, Slider

def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()
        
def save_file():
    with open(file_name.value, "w") as f:
        f.write(editor.value)
        save_button.disable()
        
def exit_app():
    #confirm_exit_banner.visible = True
    confirm_exit_banner.show()
    

def confirm_exit():
    app.destroy()
    
def change_font():
    editor.font = font.value
    
def change_text_size():
    editor.text_size = size.value
    # resize the widget because if the text is made bigger, this might affect the size of the TextBox so guizero needs to know how to maintain the intended layout
    #editor.resize(1, 1)
    editor.resize("fill", "fill")
    
def change_text_color():
    editor.text_color = color.value
    # resize the widget because if the text is made bigger, this might affect the size of the TextBox so guizero needs to know how to maintain the intended layout
    #editor.resize(1, 1)
    
def enable_save():
	save_button.enable()
    
def toggle_preferences():
    global preferences
    if not preferences:
        font.show()
        color.show()
        size.show()
        text_options_button.text="Hide Preferences"
        preferences=True
    else:
        font.hide()
        color.hide()
        size.hide()
        text_options_button.text="Show Preferences"
        preferences=False
        
        
preferences=False

app = App(title="texteditor")

# define the high level structure (4 boxes )
file_controls = Box(app, align="top", width="fill")
preferences_controls = Box(app, layout="grid", border=True)
editor_box = Box(app, align="top")
confirm_exit_banner= Box(app, visible = False, align="top")


#Define the contents of the File Controls box
# create a TextBox for the file name
file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left")
# create a save button which uses the save_file function
save_button = PushButton(file_controls, text="Save",  command = save_file, align="right")
# create an open button which uses the open_file function
open_button = PushButton(file_controls, text="Open",  align="right", command=open_file)
exit_button = PushButton(file_controls, text="Exit",  align="right", command=exit_app)

#Define the contents of the Editor box
editor = TextBox(editor_box, multiline=True, height="fill", width="fill", command= enable_save)


#Define the contents of the controls box 
text_options_button = PushButton(preferences_controls,text="show preferences", grid=[0,0], command=toggle_preferences)
font = Combo(preferences_controls, options=["courier", "times new roman", "verdana"], grid=[1,0], command=change_font, visible=False)
size = Slider(preferences_controls,  grid=[2,0], command=change_text_size, start=10, end=18, visible=False)
color = Combo(preferences_controls, options=["black","green", "red", "yellow"], grid=[3,0], command=change_text_color, visible=False)

#Define the contents of the confirm exit banner
confirm_exit_button = PushButton (confirm_exit_banner, text="confirm exit", align="right", command= confirm_exit)


app.display()