# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:01:02 2022

@author: rmh_r
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:50:54 2022

@author: rmh_r
"""


counter = ''

from os import listdir
from random import randint, shuffle
from guizero import App, Text, Box, PushButton, TextBox
def do_nothing(inputs):
    
    global counter 
    counter += inputs
    return (5)

def get_emoji_set (grid_size, grid_num):
        
    for x in range (0,grid_size):
        matched.append([])
        for y in range (0,grid_size):
            choice = randint (0,len(images))
            matched[x].append (images.pop (choice)) 
    return (matched)  



matched = []


images = listdir('./images')


grid = get_emoji_set (3,1)


print (grid)
print (grid[0][0])


app = App(title="My app", height=900, width=500, layout="grid")
text = Text(app, text="Which Is The Same", grid=[1,0])
box = Box(app, layout="grid", grid=[0,0])

input_box = TextBox(box, grid=[3,0], width=8)

button4 = PushButton(box, command=do_nothing, args=['1'], grid=[0,1], image='./images/1f1e6.gif')
button5 = PushButton(box, command=do_nothing, args=['2'], grid=[1,1], image='./images/1f69b.gif')
button6 = PushButton(box, command=do_nothing, args=['3'], grid=[2,1], image='./images/1f1e6.gif')
button7 = PushButton(box, command=do_nothing, args=['4'], grid=[0,2], image='./images/1f1e6.gif')
button8 = PushButton(box, command=do_nothing, args=['5'], grid=[1,2], image='./images/1f1e6.gif')
button9 = PushButton(box, command=do_nothing, args=['6'], grid=[2,2], image='./images/1f1e6.gif')
button10 = PushButton(box, command=do_nothing, args=['7'], grid=[0,3], image='./images/1f1e6.gif')
button11 = PushButton(box, command=do_nothing, args=['8'], grid=[1,3], image='./images/1f1e6.gif')
button12 = PushButton(box, command=do_nothing, args=['9'], grid=[2,3], image='./images/1f1e6.gif')


app.display()

print (counter)

