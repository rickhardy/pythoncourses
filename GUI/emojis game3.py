


counter = ''

from os import listdir
from random import randint, shuffle
from guizero import App, Text, Box, PushButton, TextBox


def check_answer (x):
    print (x)
    None
    
    

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
    grid[game_grid][0][0]=grid[0][0][0]
    shuffle (grid [game_grid]) 
    for ii, sublist in enumerate(grid [game_grid]): 
        shuffle(grid [game_grid][ii])
  
       
#at the end record the correct image then shuffle the first list again  
correct_image = grid[0][0][0]     
shuffle (grid [0][0])
for ii, sublist in enumerate(grid [0][0]): 
    shuffle(grid [0][ii])


app = App(title="My app", height=900, width=500, layout="grid")

buttons=[]
grid_box=[]

for grid_num in range (0, num_grids):
    grid_box.append ( Box(app, layout="grid", grid=[grid_num*2 ,0]))
    space = Text(app, text="     ", grid=[grid_num*2+1,0])
    
    for button_x in range(0,grid_size):
        for button_y in range (0,grid_size):
            buttons.append( PushButton(grid_box[grid_num], command=check_answer, args=[grid[grid_num][button_x][button_y]], grid=[button_x,button_y], image='./images/'+grid[grid_num][button_x][button_y] ))




            
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

#print (counter)

