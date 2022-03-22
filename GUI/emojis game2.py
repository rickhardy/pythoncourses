


counter = ''

from os import listdir
from random import randint, shuffle
from guizero import App, Text, Box, PushButton, TextBox
def do_nothing(inputs):
    
    global counter 
    counter += inputs
    return (5)

def get_emoji_set (grid_size):
    matched = []  
    for x in range (0,grid_size):
        matched.append([])
        
        for y in range (0,grid_size):
            choice = randint (0,len(images))
            matched[x].append (images.pop (choice)) 
    return (matched)  


grid_size=3
num_grids=2

grid=[]

images = listdir('./images')

for game_grid in range (0,num_grids):
    #print ('emojis:', get_emoji_set (3,1))
    grid.append  (get_emoji_set (grid_size))

print ('grid:', grid)

app = App(title="My app", height=900, width=500, layout="grid")
#text = Text(app, text="Which Is The Same", grid=[3,0])
#box = Box(app, layout="grid", grid=[0,0])

#input_box = TextBox(box, grid=[3,0], width=8)

buttons=[]
grid_box=[]

for grid_num in range (0, num_grids):
    grid_box.append ( Box(app, layout="grid", grid=[grid_num*2 ,0]))
    space = Text(app, text="space", grid=[grid_num*2+1,0])
    
    for button_x in range(0,3):
        for button_y in range (0,3):
            buttons.append( PushButton(grid_box[grid_num], command=do_nothing, args=['1'], grid=[button_x,button_y], image='./images/'+grid[grid_num][button_x][button_y] ))




            
#image=grid[0][0][0]
'''
button4 = PushButton(box, command=do_nothing, args=['1'], grid=[0,1], image='./images/1f1e6.gif')
button5 = PushButton(box, command=do_nothing, args=['2'], grid=[1,1], image='./images/1f69b.gif')
button6 = PushButton(box, command=do_nothing, args=['3'], grid=[2,1], image='./images/1f1e6.gif')
button7 = PushButton(box, command=do_nothing, args=['4'], grid=[0,2], image='./images/1f1e6.gif')
button8 = PushButton(box, command=do_nothing, args=['5'], grid=[1,2], image='./images/1f1e6.gif')
button9 = PushButton(box, command=do_nothing, args=['6'], grid=[2,2], image='./images/1f1e6.gif')
button10 = PushButton(box, command=do_nothing, args=['7'], grid=[0,3], image='./images/1f1e6.gif')
button11 = PushButton(box, command=do_nothing, args=['8'], grid=[1,3], image='./images/1f1e6.gif')
button12 = PushButton(box, command=do_nothing, args=['9'], grid=[2,3], image='./images/1f1e6.gif')
'''

app.display()

print (counter)

