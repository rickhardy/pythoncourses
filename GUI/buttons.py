# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:50:54 2022

@author: rmh_r
"""


counter = ''


from guizero import App, Text, Box, PushButton, TextBox
def do_nothing(inputs):
    print ("hwêllo",inputs)
    global counter 
    counter += inputs
    return (5)



app = App(title="My app", height=900, width=500, layout="grid")
text = Text(app, text="Dial First number here", grid=[1,0])
box = Box(app, layout="grid", grid=[0,0])
button1 = PushButton(box, command=do_nothing, args=['Rec'], text="Rec", grid=[0,0])
button2 = PushButton(box, command=do_nothing, args=['Call'],text="Call", grid=[1,0], width=8)

input_box = TextBox(box, grid=[3,0], width=8)

button4 = PushButton(box, command=do_nothing, args=['1'],text="1", grid=[0,1])
button5 = PushButton(box, command=do_nothing, args=['2'],text="2", grid=[1,1])
button6 = PushButton(box, command=do_nothing, args=['3'],text="3", grid=[2,1])
button7 = PushButton(box, command=do_nothing, args=['4'],text="4", grid=[0,2])
button8 = PushButton(box, command=do_nothing, args=['5'],text="5", grid=[1,2])
button9 = PushButton(box, command=do_nothing, args=['6'],text="6", grid=[2,2])
button10 = PushButton(box, command=do_nothing, args=['7'],text="7", grid=[0,3])
button11 = PushButton(box, command=do_nothing, args=['8'],text="8", grid=[1,3])
button12 = PushButton(box, command=do_nothing, args=['9'],text="9", grid=[2,3])
button13 = PushButton(box, command=do_nothing, args=['0'],text="0", grid=[1,4])

text = Text(app, text="Dial second number here", grid=[0,3])
box2 = Box(app, layout="grid", grid=[1,3], visible=True )
button21 = PushButton(box2, command=do_nothing, text="Rec", grid=[0,0])
button22 = PushButton(box2, command=do_nothing, text="Call", grid=[1,0], width=8)
button24 = PushButton(box2, command=do_nothing, text="1", grid=[0,1])
button25 = PushButton(box2, command=do_nothing, text="2", grid=[1,1])
button26 = PushButton(box2, command=do_nothing, text="3", grid=[2,1])
button27 = PushButton(box2, command=do_nothing, text="4", grid=[0,2])
button27 = PushButton(box2, command=do_nothing, text="5", grid=[1,2])
button29 = PushButton(box2, command=do_nothing, text="6", grid=[2,2])
button210 = PushButton(box2, command=do_nothing, text="7", grid=[0,3])
button211 = PushButton(box2, command=do_nothing, text="8", grid=[1,3])
button212 = PushButton(box2, command=do_nothing, text="9", grid=[2,3])
button213 = PushButton(box2, command=do_nothing, text="0", grid=[1,4])

app.display()

print (counter)

